from flask import render_template,request,redirect
from flask_login import login_required,current_user
from . import main
from ..models import User,Pitch,Comment
from .forms import CommentForm

@main.route('/')
@login_required
def index():

    title = 'Home - Just Pitch Out'

    bootcamp_piches = Pitch.get_pitches('bootcamp')
    trip_piches = Pitch.get_pitches('trip')
    sports_pitches = Pitch.get_pitches('sports')
    return render_template('index.html', title=title, bootcamp = bootcamp_pitches, trip = trip_pitches, sports = sports_pitches)

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
