from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from app import app, db
from models import User, Song, Playlist, Item
from flask import render_template, request, url_for, redirect, flash

#A form for inputing new songs via Dashboard
class SongForm(FlaskForm):
  title = StringField(label = "Song Title:", validators=[DataRequired()])
  artist = StringField(label = "Artist:", validators=[DataRequired()])
  submit = SubmitField("Add Song")


"""
ADD a UserForm(FlaskForm) that allows the Admin to create new users

Also gives Admin the ability to delete users
"""




#A function we made to check if an item to be added is already in the playlist
def exists(item, playlist):
  """Return a boolean
    True if playlist contains item. False otherwise.
    """
  for i in playlist: #for each item in playlist
    if i.song_id == item.song_id: #check if the primary key is equal
       return True
  return False



#The home page of FlaskFM
#Lists all the users currently in the database
#renders the home.html template providing the list of current users
@app.route('/profiles')
def profiles():
    #current_users = [] #change here to a database query
    current_users = User.query.all()

    return render_template('users.html', current_users = current_users)



#Displays profile pages for a user with the user_id primary key
#renders the profile.html template for a specific user, song library and 
#the user's playlist 
@app.route('/profile/<int:user_id>')
def profile(user_id):
  
  user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")

  songs = Song.query.all()
  #raw_songs = Song.query.filter_bys
  #that user's playlist id is then queried from the Playlist table
  my_playlist = Playlist.query.get(user.playlist_id) #change here to a database query

  #needed = Song.query.get(my_playlist.items.song_id)

  return render_template('profile.html', template_user = user, template_songs = songs, template_my_playlist = my_playlist)



#Adds new songs to a user's playlist from the song library
#redirects back to the profile that issued the addition
@app.route('/add_item/<int:user_id>/<int:song_id>/<int:playlist_id>')
def add_item(user_id, song_id, playlist_id):
   new_item = Item(song_id = song_id, playlist_id = playlist_id)
   user = User.query.filter_by(id = user_id).first_or_404(description = "No such user found.")
   my_playlist = Playlist.query.filter_by(id = user.playlist_id).first()

   if not exists(new_item, my_playlist.items):
      song = Song.query.get(song_id)
      #using db session add the new item
      db.session.add(new_item)
      #increase the counter for the song associated with the new item
      song.n +=1
      #commit the database changes here
      db.session.commit()
   return redirect(url_for('profile', user_id = user_id))



#Remove a song from the available Songs() visible from the dashboard
#Redirects back to the dashboard
@app.route('/remove_song/<int:song_id>')
def remove_song(song_id):
  

  #from the Item model, fetch the item with primary key item_id to be deleted
  removed_song = Song.query.get(song_id)
  #using db.session delete the item
  db.session.delete(removed_song)
  #commit the deletion
  db.session.commit()

  #call this function in order to remove any playlist Items() which contain the deleted song
  delete_removed_song_from_users_playlists(song_id)

  return redirect(url_for('dashboard'))


#Function which will check each user's playlist.item.song's and see if it matches a newly deleted song from the admin page\
# if found, remove it from the playlist
def delete_removed_song_from_users_playlists(deleted_song_id):

  #query all the Item() objects
  items = Item.query.all()

  #search each item's song_id attr, and delete accordingly
  for item in items:
    if item.song_id == deleted_song_id:
      db.session.delete(item); db.session.commit()





#Display the Dashboard page with a form for adding songs
#Renders the dashboard template
@app.route('/dashboard', methods=["GET", "POST"])
def dashboard():
  # this SongForm() is what is lcoated in the dashboard.html code. 
  form = SongForm(csrf_enabled=False)

  if request.method == 'POST' and form.validate():
  
    #create the new_song data entry of the Song schema
    new_song = Song(title = form.title.data, artist = form.artist.data, n = 1)
    #add it to the database
    db.session.add(new_song)
    #commit to the database
    db.session.commit()

  else:
    flash(form.errors)


  #query the 'n' - star attribute, and sort them in descending order
  popular_songs = Song.query.order_by(Song.n.desc())  

  popular_songs = popular_songs[:5]

  #call this Song() instance here because it now will include the updated user's 'new_song' committed to the Song() table
  songs = Song.query.all()
  return render_template('dashboard.html', songs = songs, template_popular_songs = popular_songs, form = form)


#Remove an item from a user's playlist
#Redirects back to the profile that issues the removal
@app.route('/remove_item/<int:user_id>/<int:item_id>')
def remove_item(user_id, item_id):
   #from the Item model, fetch the item with primary key item_id to be deleted
   removed_item = Item.query.get(item_id)
   #using db.session delete the item
   db.session.delete(removed_item)
   #commit the deletion
   db.session.commit()

   return redirect(url_for('profile', user_id = user_id))


