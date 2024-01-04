# game.py: define the form for the scout page

# Below is an example from Charged Up 2023.

from flask_wtf import FlaskForm
from wtforms import IntegerField, RadioField, TextAreaField
from wtforms.validators import *

class ChargedUpScoutForm(FlaskForm):
    name = "Charged Up 2023"

    matchNum = IntegerField('matchNumber', validators=[DataRequired()])
    teamNum = IntegerField('teamNumber', validators=[DataRequired()])

    autoHighCones = IntegerField('autoHighCones', validators=[DataRequired()], default=0)
    autoHighCubes = IntegerField('autoHighCubes', validators=[DataRequired()], default=0)
    autoMidCones = IntegerField('autoMidCones', validators=[DataRequired()], default=0)
    autoMidCubes = IntegerField('autoMidCubes', validators=[DataRequired()], default=0)
    autoLowCones = IntegerField('autoLowCones', validators=[DataRequired()], default=0)
    autoLowCubes = IntegerField('autoLowCubes', validators=[DataRequired()], default=0)
    teleopHighCones = IntegerField('teleopHighCones', validators=[DataRequired()], default=0)
    teleopHighCubes = IntegerField('teleopHighCubes', validators=[DataRequired()], default=0)
    teleopMidCones = IntegerField('teleopMidCones', validators=[DataRequired()], default=0)
    teleopMidCubes = IntegerField('teleopMidCubes', validators=[DataRequired()], default=0)
    teleopLowCones = IntegerField('teleopLowCones', validators=[DataRequired()], default=0)
    teleopLowCubes = IntegerField('teleopLowCubes', validators=[DataRequired()], default=0)

    defense = RadioField('defense', validators=[DataRequired()], choices=[
        ('none', 'Did not play defense'),
        ('poor', 'Poor defense'),
        ('average', 'Average defense'),
        ('excellent', 'Excellent defense!')
    ])

    sub = RadioField('sub', validators=[DataRequired()], choices=[
        ('single', 'Single substation'),
        ('double', 'Double substation'),
        ('both', 'Used both substations'),
    ])

    droppedPieces = IntegerField('Dropped Pieces', validators=[DataRequired()])

    info = TextAreaField('info', validators=[DataRequired()])

class UltimateAscentScoutForm(FlaskForm):
    name = "Ultimate Ascent 2013"

    matchNum = IntegerField('matchNumber', validators=[DataRequired()])
    teamNum = IntegerField('teamNumber', validators=[DataRequired()])

    discsScored = IntegerField('discsScored', validators=[DataRequired()])
    discsMissed = IntegerField('discsMissed', validators=[DataRequired()])

    climb = RadioField('climb', validators=[DataRequired()], choices=[
        (0, 'No climb'),
        (1, 'First level'),
        (2, 'Second level'),
        (3, 'Third level'),
    ])

    info = TextAreaField('info', validators=[DataRequired()])

class CrescendoForm(FlaskForm):
    name = "Crescendo 2024"

    matchNum = IntegerField('matchNumber', validators=[DataRequired()])
    teamNum = IntegerField('teamNumber', validators=[DataRequired()])

    ### Insert new fields here ###

    info = TextAreaField('info', validators=[DataRequired()])