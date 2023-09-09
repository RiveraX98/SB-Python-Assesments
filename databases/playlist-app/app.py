from flask import Flask, redirect, render_template,flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Playlist, Song, PlaylistSong
from forms import NewSongForPlaylistForm, SongForm, PlaylistForm

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///playlists'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "Keyabc123"



connect_db(app)
db.create_all()
debug = DebugToolbarExtension(app)


# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False




@app.route("/")
def root():
    """Homepage: redirect to /playlists."""
    

    return redirect("/playlists")


##############################################################################
# Playlist routes


@app.route("/playlists")
def show_all_playlists():
    """Return a list of playlists."""

    playlists = Playlist.query.all()
    return render_template("playlists.html", playlists=playlists)


@app.route("/playlists/<int:playlist_id>")
def show_playlist(playlist_id):
    """Show detail on specific playlist."""
    playlist = Playlist.query.get_or_404(playlist_id)

    return render_template("playlist.html", playlist= playlist)


@app.route("/playlists/add", methods=["GET", "POST"])
def add_playlist():
    """Handle add-playlist form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-playlists
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form=PlaylistForm()
    if form.validate_on_submit():
        name = form.name.data
        description= form.description.data
        new_playlist = Playlist(name=name, description= description)
        db.session.add(new_playlist)
        db.session.commit()
        flash("playlist added successfully", "success")
        return redirect("/playlists")
    else:
        return render_template("new_playlist.html", form = form)




##############################################################################
# Song routes


@app.route("/songs")
def show_all_songs():
    """Show list of songs."""

    songs = Song.query.all()
    return render_template("songs.html", songs=songs)


@app.route("/songs/<int:song_id>")
def show_song(song_id):
    """return a specific song"""
    song = Song.query.get_or_404(song_id)
    return render_template("song.html", song=song )

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK


@app.route("/songs/add", methods=["GET", "POST"])
def add_song():
    """Handle add-song form:

    - if form not filled out or invalid: show form
    - if valid: add playlist to SQLA and redirect to list-of-songs
    """

    # ADD THE NECESSARY CODE HERE FOR THIS ROUTE TO WORK
    form = SongForm()
    if form.validate_on_submit():
        artist = form.artist.data
        title = form.title.data
        new_song= Song(artist=artist, title=title)
        db.session.add(new_song)
        db.session.commit()
        song= Song.query.filter_by(title=title, artist=artist).first()
        flash("song added successfully", "success")
        return redirect(f"/songs/{song.id}")
    else:
        return render_template("new_song.html", form=form)



@app.route("/playlists/<int:playlist_id>/add_song", methods=["GET", "POST"])
def show_playlist_page(playlist_id):
    """Add a playlist and redirect to list."""

  
    
    playlist = Playlist.query.get_or_404(playlist_id)

    form = NewSongForPlaylistForm()
    

    curr_on_playlist = [song.id for song in playlist.songs]
    form.song.choices = db.session.query(Song.id, Song.title).filter(Song.id.notin_(curr_on_playlist)).all()

    if form.validate_on_submit():
          song= form.song.data
          new_playlistSong=PlaylistSong(playlist_id =None,song_id=song)
          db.session.add(new_playlistSong)
          db.session.commit()
          flash("Song added to playlists", "success")

          return redirect(f"/playlists/{playlist_id}")

    return render_template("add_song_to_playlist.html", playlist=playlist,form=form)



# @app.route("/playlists/<int:playlist_id>/add-song", methods= ["POST"])
# def add_song_to_playlist(playlist_id):
#         form = NewSongForPlaylistForm()
#         form.validate_on_submit()
#         song= form.song.data
#         new_playlistSong=PlaylistSong(playlist_id =None,song_id=song)
#         db.session.add(new_playlistSong)
#         db.session.commit()
#         # flash("Song added to playlists", "success")

#         # return redirect(f"/playlists/{playlist_id}")