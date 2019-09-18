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