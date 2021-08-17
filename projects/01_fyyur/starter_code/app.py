#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

import json
import sys
import dateutil.parser
import babel
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_moment import Moment
from flask_migrate import Migrate
import logging
from logging import Formatter, FileHandler
# from flask_wtf import FlaskForm
from forms import *

from models import db, Artist, Venue, Show

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
moment = Moment(app)


# TODO: connect to a local postgresql database
app.config.from_object('config')
db.init_app(app)

# For Migration
migrate = Migrate(app, db)

#----------------------------------------------------------------------------#
# Filters.
#----------------------------------------------------------------------------#

def format_datetime(value, format='medium'):
  date = dateutil.parser.parse(value)
  if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
  elif format == 'medium':
      format="EE MM, dd, y h:mma"
  return babel.dates.format_datetime(date, format, locale='en')

app.jinja_env.filters['datetime'] = format_datetime

#----------------------------------------------------------------------------#
#                                 Main Route
#----------------------------------------------------------------------------#

@app.route('/')
def index():
  return render_template('pages/home.html')

#  ----------------------------------------------------------------
#                             Venues
#  ----------------------------------------------------------------

@app.route('/venues')
def venues():
  # TODO: replace with real venues data.
  # num_upcoming_shows should be aggregated based on number of upcoming shows per venue.
  city_list = Venue.query.distinct(Venue.city).all()
  data = []
  
  for city in city_list:
    venue_in_city = {
      "city": city.city,
      "state": city.state,
      "venues": []
    }
    for venue_data in Venue.query.all():
      if venue_data.city == city.city and venue_data.state == venue_data.state:
        venue_in_city['venues'].append({
          "id": venue_data.id,
          "name": venue_data.name,
          # fix
          "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id == Venue.id).filter(Show.start_time >datetime.now()).all()),
        })
    data.append(venue_in_city)
    
  return render_template('pages/venues.html', areas=data);

# Task Completed
@app.route('/venues/search', methods=['POST'])
def search_venues():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for Hop should return "The Musical Hop".
  # search for "Music" should return "The Musical Hop" and "Park Square Live Music & Coffee"
  kw_search = request.form['search_term']
  search_result = Venue.query.filter(Venue.name.ilike(f'%{kw_search}%')).all(),
  data = []
  for result in search_result[0]:
    data.append({
      "id": result.id,
      "name": result.name,
      "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id == result.id).filter(Show.start_time > datetime.now()).all()),
    })

  response={
    "count": len(search_result[0]),
    "data": data,
  }
  return render_template('pages/search_venues.html', results=response, search_term=request.form.get('search_term', ''))

# Task Completed
@app.route('/venues/<int:venue_id>')
def show_venue(venue_id):
  # shows the venue page with the given venue_id
  # TODO: replace with real venue data from the venues table, using venue_id
  data = []
  venues = Venue.query.all()

  past_shows_query = db.session.query(Show).join(Artist).filter(Show.venue_id == venue_id).filter(Show.start_time < datetime.now()).all(),
  upcoming_shows_query = db.session.query(Show).join(Artist).filter(Show.venue_id == venue_id).filter(Show.start_time > datetime.now()).all(),
  past_shows = []
  upcoming_shows = []

  for show in past_shows_query[0]:
    past_shows.append({
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    })
  for show in upcoming_shows_query[0]:
    upcoming_shows.append({
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S")  
    })

  datalist = []
  for venue in venues:
    genres_list = venue.genres[1:-1].replace('\'',"").replace('\"',"").split(',')
    datalist.append({
      "id": venue.id,
      "name": venue.name,
      "genres": genres_list,
      "address": venue.address,
      "city": venue.city,
      "state": venue.state,
      "phone": venue.phone,
      "website": venue.website,
      "facebook_link": venue.facebook_link,
      "seeking_talent": venue.seeking_telent,
      "image_link": venue.image_link,
      "seeking_description": venue.seeking_description,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": len(past_shows),
      "upcoming_shows_count": len(upcoming_shows),
    })
  try:
    data = list(filter(lambda d: d['id'] == venue_id, datalist ))[0]
    return render_template('pages/show_venue.html', venue=data)
  except IndexError:
    return render_template('errors/404.html')
  
#  ----------------------------------------------------------------
#  Create Venue
#  ----------------------------------------------------------------
# No Need to Modify
@app.route('/venues/create', methods=['GET'])
def create_venue_form():
  form = VenueForm()
  return render_template('forms/new_venue.html', form=form)


# Task Completed
@app.route('/venues/create', methods=['POST'])
def create_venue_submission():
  # TODO: insert form data as a new Venue record in the db, instead
  # TODO: modify data to be the data object returned from db insertion

  def form_null_check(filed_name):
    if not request.form[filed_name]:
      result = ""
    else:
      result = request.form[filed_name]
    return result

  # TODO: modify data to be the data object returned from db insertion
  try:
    venue = Venue(
      name=form_null_check('name'),
      genres= request.form.getlist('genres'),
      address = form_null_check('address'),
      city=form_null_check('city'),
      state=form_null_check('state'),
      phone=form_null_check('phone'),
      website=form_null_check('website_link'),
      facebook_link=form_null_check('facebook_link'),
      seeking_telent = True if 'seeking_talent' in request.form else False,
      seeking_description=form_null_check('seeking_description'),
      image_link=form_null_check('image_link'),
    )
    db.session.add(venue)
    db.session.commit()
    db.session.close()
  # on successful db insert, flash success
    flash('Venue ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  except :
    db.session.rollback()
    db.session.close()
    flash('An error occurred. Venue ' + request.form['name'] + ' could not be listed.')
  # e.g., flash('An error occurred. Venue ' + data.name + ' could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

#  ----------------------------------------------------------------
#                             Delete
#  ----------------------------------------------------------------
# Task Completed
@app.route('/venues/<venue_id>', methods=['DELETE'])
def delete_venue(venue_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  try:
    # venue_delete = Venue.query.get(venue_id)
    db.session.query(Venue).filter(Venue.id == venue_id).delete()
    db.session.commit()
    flash(f"Venue {venue_id } was successfully deleted")
  except:
    print(sys.exc_info())
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for("index"))

# Task Completed
@app.route('/artist/<artist_id>', methods=['DELETE'])
def delete_artist(artist_id):
  # TODO: Complete this endpoint for taking a venue_id, and using
  # SQLAlchemy ORM to delete a record. Handle cases where the session commit could fail.
  try:
    # venue_delete = Venue.query.get(venue_id)
    db.session.query(Artist).filter(Artist.id == artist_id).delete()
    db.session.commit()
    flash(f"Artist { artist_id } was successfully deleted")
  except:
    print(sys.exc_info())
    db.session.rollback()
  finally:
    db.session.close()
  return redirect(url_for("index"))
  
#  ----------------------------------------------------------------
#                             Artists
#  ----------------------------------------------------------------
#Completed
@app.route('/artists')
def artists():
  # TODO: replace with real data returned from querying the database
  artists = Artist.query.all()
  data = []
  for artist in artists:
    data.append({
      'id': artist.id,
      'name': artist.name,
    })
  return render_template('pages/artists.html', artists=data)

# Task Completed
@app.route('/artists/search', methods=['POST'])
def search_artists():
  # TODO: implement search on artists with partial string search. Ensure it is case-insensitive.
  # seach for "A" should return "Guns N Petals", "Matt Quevado", and "The Wild Sax Band".
  # search for "band" should return "The Wild Sax Band".
  kw_search = request.form['search_term']
  search_result = Artist.query.filter(Artist.name.ilike(f'%{kw_search}%')).all(),
  data = []
  for result in search_result[0]:
    data.append({
      "id": result.id,
      "name": result.name,
      "num_upcoming_shows": len(db.session.query(Show).filter(Show.venue_id == result.id).filter(Show.start_time > datetime.now()).all()),
  })

  response={
    "count": len(search_result[0]),
    "data": data,
  }
  return render_template('pages/search_artists.html', results=response, search_term=request.form.get('search_term', ''))

# Not Completed
@app.route('/artists/<int:artist_id>')
def show_artist(artist_id):
  # shows the artist page with the given artist_id
  # TODO: replace with real artist data from the artist table, using artist_id
  artists = Artist.query.all()
  datalist = []
  past_shows_query = db.session.query(Show).join(Venue).filter(Show.artist_id == artist_id).filter(Show.start_time < datetime.now()).all(),
  upcoming_shows_query = db.session.query(Show).join(Venue).filter(Show.artist_id == artist_id).filter(Show.start_time > datetime.now()).all(),

  past_shows = []
  upcoming_shows = []

  for show in past_shows_query[0]:
    past_shows.append({
       "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "venue_image_link": show.venue.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    })
  for show in upcoming_shows_query[0]:
    upcoming_shows.append({
      "artist_id": show.artist_id,
      "artist_name": show.artist.name,
      "venue_image_link": show.venue.image_link,
      "start_time": show.start_time.strftime("%Y-%m-%d %H:%M:%S")  
    })

  for artist in artists:
    genres_list = artist.genres[1:-1].replace('\'',"" ).replace('\"',"").split(',')  
    datalist.append({
      "id": artist.id,
      "name": artist.name,
      "genres": genres_list,
      "city": artist.city,
      "state": artist.state,
      "phone": artist.phone,
      "website": artist.website,
      "facebook_link": artist.facebook_link,
      "seeking_venue": artist.seeking_venue,
      "image_link": artist.image_link,
      "seeking_description": artist.seeking_description,
      "past_shows": past_shows,
      "upcoming_shows": upcoming_shows,
      "past_shows_count": len(past_shows),
      "upcoming_shows_count": len(upcoming_shows),
    })

  try:
    data = list(filter(lambda d: d['id'] == artist_id, datalist ))[0]
    return render_template('pages/show_artist.html', artist=data)
  except IndexError:
    return render_template('errors/404.html')


#  ----------------------------------------------------------------
#                             Update
#  ----------------------------------------------------------------
# Task Completed
@app.route('/artists/<int:artist_id>/edit', methods=['GET'])
def edit_artist(artist_id):
  form = ArtistForm()
  artist_query = Artist.query.filter_by(id=artist_id).first()
  artist={
    "id": artist_query.id,
    "name": artist_query.name,
    "genres": artist_query.genres,
    "city": artist_query.city,
    "state": artist_query.state,
    "phone": artist_query.phone,
    "website": artist_query.website,
    "facebook_link": artist_query.facebook_link,
    "seeking_venue": artist_query.seeking_venue,
    "seeking_description": artist_query.seeking_description,
    "image_link": artist_query.image_link,
  }
  # TODO: populate form with fields from artist with ID <artist_id>
  return render_template('forms/edit_artist.html', form=form, artist=artist)

# Task Completed
@app.route('/artists/<int:artist_id>/edit', methods=['POST'])
def edit_artist_submission(artist_id):
  # TODO: take values from the form submitted, and update existing
  # artist record with ID <artist_id> using the new attributes
  error = False
  artist = Artist.query.filter_by(id=artist_id).one()
  try:
    artist.name = request.form['name']
    # fixed
    artist.genres = request.form.getlist('genres')
    artist.city = request.form['city']
    artist.state = request.form['state']
    artist.phone = request.form['phone']
    artist.website = request.form['website_link']
    artist.facebook_link = request.form['facebook_link']
    # fixed
    artist.seeking_venue = True if 'seeking_venue' in request.form else False
    artist.seeking_description = request.form['seeking_description']
    artist.image_link = request.form['image_link']
    db.session.add(artist)
    db.session.commit()
  except :
    error = True
    db.session.rollback()
  finally:
    db.session.close()
  if error: 
    flash('An error occurred. Artist could not be updated.')
  if not error: 
    flash('Artist was successfully updated!')
  return redirect(url_for('show_artist', artist_id=artist_id))

# Task Completed
@app.route('/venues/<int:venue_id>/edit', methods=['GET'])
def edit_venue(venue_id):
  form = VenueForm()
  # TODO: populate form with values from venue with ID <venue_id>
  venue_query = Venue.query.filter_by(id=venue_id).first()
  venue={
    "id": venue_query.id,
    "name": venue_query.name,
    "genres": venue_query.genres,
    "address": venue_query.address,
    "city": venue_query.city,
    "state": venue_query.state,
    "phone": venue_query.phone,
    "website": venue_query.website,
    "facebook_link": venue_query.facebook_link,
    "seeking_talent": venue_query.seeking_telent,
    "seeking_description": venue_query.seeking_description,
    "image_link": venue_query.image_link,
  }
  return render_template('forms/edit_venue.html', form=form, venue=venue)

# Task Completed
@app.route('/venues/<int:venue_id>/edit', methods=['POST'])
def edit_venue_submission(venue_id):
  # TODO: take values from the form submitted, and update existing
  # venue record with ID <venue_id> using the new attributes
  venue = Venue.query.filter_by(id=venue_id).one()
  error = False

  try:
    venue.name = request.form['name']
    # fixed
    venue.genres = request.form.getlist('genres')
    venue.address = request.form['address']
    venue.city = request.form['city']
    venue.state = request.form['state']
    venue.phone = request.form['phone']
    venue.website = request.form['website_link']
    venue.facebook_link = request.form['facebook_link']
    # fixed
    venue.seeking_telent = True if 'seeking_telent' in request.form else False
    venue.seeking_description = request.form['seeking_description']
    venue.image_link = request.form['image_link']
    db.session.add(venue)
    db.session.commit()
  except :
    error = True
    db.session.rollback()
  finally:
    db.session.close()
  if error: 
    flash(f'An error occurred. Venue could not be updated.')
  if not error: 
    flash(f'Venue was successfully updated!')
  return redirect(url_for('show_venue', venue_id=venue_id))

#  ----------------------------------------------------------------
#  Create Artist
#  ----------------------------------------------------------------

# No Need to Modify
@app.route('/artists/create', methods=['GET'])
def create_artist_form():
  form = ArtistForm()
  return render_template('forms/new_artist.html', form=form)

#Task Completed
@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
  # called upon submitting the new artist listing form
  # TODO: insert form data as a new Venue record in the db, instead
  def form_null_check(filed_name):
    if not request.form[filed_name]:
      result = ""
    else:
      result = request.form[filed_name]
    return result
  # TODO: modify data to be the data object returned from db insertion
  try:
    artist = Artist(
      name=form_null_check('name'),
      genres=request.form.getlist('genres'),
      city=form_null_check('city'),
      state=form_null_check('state'),
      phone=form_null_check('phone'),
      website=form_null_check('website_link'),
      facebook_link=form_null_check('facebook_link'),
      # fixed
      seeking_venue = True if 'seeking_venue' in request.form else False,
      seeking_description=form_null_check('seeking_description'),
      image_link=form_null_check('image_link'),
    )
    db.session.add(artist)
    db.session.commit()
    db.session.close()
  # on successful db insert, flash success
    flash('Artist ' + request.form['name'] + ' was successfully listed!')
  # TODO: on unsuccessful db insert, flash an error instead.
  except:
    db.session.rollback()
    db.session.close()
    print(Exception)
    flash('An error occurred. Artist ' + request.form['name'] + ' could not be listed.')
  # e.g., flash('An error occurred. Artist ' + data.name + ' could not be listed.')
  return render_template('pages/home.html')

#  ----------------------------------------------------------------
#  Shows
#  ----------------------------------------------------------------


# Task Completed
@app.route('/shows')
def shows():
  # displays list of shows at /shows
  # TODO: replace with real venues data.
  #show_data = db.session.query(show_table).join(Artist).join(Venue).all()
  show_data = Show.query.join(Artist, Artist.id == Show.artist_id).join(Venue,Venue.id == Show.venue_id).all()
  #print(show_data)
  data = []
  for show in show_data:
    data.append({
      "venue_id": show.venue_id,
      "venue_name": show.venue.name,
      "artist_id": show.artist_id,
      "artist_name": show.artist.name, 
      "artist_image_link": show.artist.image_link,
      "start_time": show.start_time.strftime('%Y-%m-%d %H:%M:%S')
    })
  return render_template('pages/shows.html', shows=data)

@app.route('/shows/create')
def create_shows():
  # renders form. do not touch.
  form = ShowForm()
  return render_template('forms/new_show.html', form=form)

@app.route('/shows/create', methods=['POST'])
def create_show_submission():
  # called to create new shows in the db, upon submitting new show listing form
  # TODO: insert form data as a new Show record in the db, instead
  def form_null_check(filed_name):
    if not request.form[filed_name]:
      result = ""
    else:
      result = request.form[filed_name]
    return result
  # TODO: modify data to be the data object returned from db insertion
  try:
    show = Show(
      artist_id = form_null_check('artist_id'),
      venue_id = form_null_check('venue_id'),
      start_time = form_null_check('start_time'),
    )
    db.session.add(show)
    db.session.commit()
  # on successful db insert, flash success
    flash('Show Created Successfully!')
  # TODO: on unsuccessful db insert, flash an error instead.
  except:
    db.session.rollback()
    flash('An error occurred. Show counldn\'t create.')
  finally:
    db.session.close()
  # TODO: on unsuccessful db insert, flash an error instead.
  # e.g., flash('An error occurred. Show could not be listed.')
  # see: http://flask.pocoo.org/docs/1.0/patterns/flashing/
  return render_template('pages/home.html')

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('errors/500.html'), 500


if not app.debug:
    file_handler = FileHandler('error.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('errors')

#----------------------------------------------------------------------------#
# Launch.
#----------------------------------------------------------------------------#

# Default port:
if __name__ == '__main__':
  app.run()

# Or specify port manually:
'''
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
'''
