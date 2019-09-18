from flask import render_template
from flask_login import login_required
from . import main

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