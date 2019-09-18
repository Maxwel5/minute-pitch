from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from . import main
from ..models import User,Pitch,Comment
from .forms import CommentForm,PitchForm

@main.route('/')
@login_required
def index():

    title = 'Home - Just Pitch Out'

    bootcamp_piches = Pitch.get_pitches('bootcamp')
    trip_piches = Pitch.get_pitches('trip')
    sports_pitches = Pitch.get_pitches('sports')
    return render_template('index.html', title=title, bootcamp = bootcamp_pitches, trip = trip_pitches, sports = sports_pitches)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username = username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path 
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user, pitches = pitches_count)
    pitches_count = Pitch.count_pitches(username)


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
        pitch = pitch_form.text.data
        title = pitch_form.title.data

        new_pitch = Pitch(pitch_title=title,pitch_content=pitch,category=category,user=current_user,likes=0,dislikes=0)

        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('pitch.html',title = title,pitch_form=pitch_form )

@main.route('/bootcamp/pitches')
def bootcamp():
    pitches = Pitch.get_pitches(bootcamp)
    return render_template('bootcamp.html', title = title, pitches = pitches)

@main.route('/trip/pitches')
def trip():
    pitches = Pitch.get_pitches(trip)
    return render_template('trip.html', title = title, pitches = pitches)

@main.route('/sports/pitches')
def sports():
    pitches = Pitch.get_pitches(sports)
    return render_template('sports.html', title = title, pitches = pitches)

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
