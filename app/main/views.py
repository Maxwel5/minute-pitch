from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from . import main
from ..models import User,Pitch,Comment
from .. import db,photos
from .forms import CommentForm,PitchForm,UpdateProfile

@main.route('/')
def index():

    title = 'Home - Just Pitch Out'

    bootcamp_pitches = Pitch.get_pitches('bootcamp')
    trip_pitches = Pitch.get_pitches('trip')
    sports_pitches = Pitch.get_pitches('sports')
    return render_template('index.html',current_user=current_user, title=title, bootcamp = bootcamp_pitches, trip = trip_pitches, sports = sports_pitches)

# @main.route('/movie/review/new/<int:id>', methods = ['GET','POST'])
# @login_required
# def new_review(id)

@main.route('/user/<username>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route('/user')

def profile():
    username = current_user.username
    user = User.query.filter_by(username = username).first()
    pitches_count = Pitch.count_pitches(username)

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches = pitches_count)
    


@main.route('/user/<username>/update',methods = ['GET','POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',username=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/pitch/new', methods = ['GET','POST'])
@login_required
def new_pitch():
    pitch_form = PitchForm()
    if pitch_form.validate_on_submit():
        category = pitch_form.category.data
        pitch = pitch_form.pitch.data
        title = pitch_form.title.data

        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,upvote=0,downvote=0)

        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html',title = title,pitch_form=pitch_form )

@main.route('/bootcamp/pitches')
def bootcamp():
    pitches = Pitch.get_pitches('bootcamp')
    return render_template('bootcamp.html', pitches = pitches)

@main.route('/trips/pitches')
def trips():
    pitches = Pitch.get_pitches('trips')
    return render_template('trips.html', pitches = pitches)

@main.route('/sports/pitches')
def sports():
    pitches = Pitch.get_pitches('sports')
    return render_template('sports.html', pitches = pitches)

@main.route('/pitch/<int:id>', methods = ['GET', 'POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)

    if request.args.get('upvote'):
        pitch.upvote = pitch.upvote + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".f(pitch_id=pitch.i))

    elif request.args.get("downvote"):
        pitch.downvote = pitch.downvote + 1

        db.session.add(pitch)
        db.session.commit()

        return redirect("/pitch/{pitch_id}".format(pitch_id=pitch.id))

    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.text.data

        new_comment = Comment(comment = comment,user = current_user,pitch_id = pitch)

        new_comment.save_comment()


    comments = Comment.get_comments(pitch)

    return render_template("pitch.html", pitch = pitch, comment_form = comment_form, comments = comments)

@main.route('/user/<username>/pitches')
def user_pitches(username):
    user = User.query.filter_by(username=username).first()
    pitches = Pitch.query.filter_by(user_id = user.id).all()
    pitches_count = Pitch.count_pitches(username)

    return render_template("profile/pitches.html", user=user,pitches=pitches,pitches_count=pitches_count)
