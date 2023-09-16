"""Forms for playlist app."""

from wtforms import StringField, SelectField, TextAreaField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""
    name = StringField("Name:", validators=[InputRequired()])
    description = TextAreaField("Discription:",  validators=[InputRequired()] )
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    artist= StringField("Artist:", validators=[InputRequired()])
    title= StringField("Title:",validators=[InputRequired()])
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add :', coerce=str )
