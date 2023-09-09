"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Playlist(db.Model):
    """Playlist."""
    __tablename__ = "playlists"

    def __repr__(self):
        return f"<PlayList{self.id}{self.name}{self.description}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String)
    
    songs = db.relationship("Song", secondary="playlists_songs", backref="playlists")

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""
    __tablename__ = "songs"

    def __repr__(self):
        return f"<Song{self.id}{self.title}{self.artist}"

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    title = db.Column(db.String(20), nullable = False)
    artist = db.Column(db.String(20), nullable = False)




    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""
    __tablename__ = "playlists_songs"

    def __repr__(self):
        return f"<Song{self.id}{self.playlist_id}{self.song_id}"

    id= db.Column(db.Integer,primary_key=True,autoincrement=True)
    playlist_id = db.Column(db.Integer, db.ForeignKey("playlists.id"))
    song_id = db.Column(db.Integer, db.ForeignKey("songs.id"))



    # ADD THE NECESSARY CODE HERE



