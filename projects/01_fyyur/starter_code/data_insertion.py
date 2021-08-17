from app import Venue, Artist, Show, db

data1={
    "id": 1,
    "name": "The Musical Hop",
    "genres": "Jazz, Reggae, Swing, Classical, Folk",
    "address": "1015 Folsom Street",
    "city": "San Francisco",
    "state": "CA",
    "phone": "123-123-1234",
    "website": "https://www.themusicalhop.com",
    "facebook_link": "https://www.facebook.com/TheMusicalHop",
    "seeking_talent": True,
    "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
    "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    "past_shows": [{
      "artist_id": 4,
      "artist_name": "Guns N Petals",
      "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
      "start_time": "2019-05-21T21:30:00.000Z"
    }],
    "upcoming_shows": [],
    "past_shows_count": 1,
    "upcoming_shows_count": 0,
}
data2={
  "id": 2,
  "name": "The Dueling Pianos Bar",
  "genres": ["Classical", "R&B", "Hip-Hop"],
  "address": "335 Delancey Street",
  "city": "New York",
  "state": "NY",
  "phone": "914-003-1132",
  "website": "https://www.theduelingpianos.com",
  "facebook_link": "https://www.facebook.com/theduelingpianos",
  "seeking_talent": False,
  "seeking_description": "",
  "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
  "past_shows": [],
  "upcoming_shows": [],
  "past_shows_count": 0,
  "upcoming_shows_count": 0,
}
data3={
  "id": 3,
  "name": "Park Square Live Music & Coffee",
  "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
  "address": "34 Whiskey Moore Ave",
  "city": "San Francisco",
  "state": "CA",
  "phone": "415-000-1234",
  "website": "https://www.parksquarelivemusicandcoffee.com",
  "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
  "seeking_talent": False,
  "seeking_description": "",
  "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
  "past_shows": [{
    "artist_id": 5,
    "artist_name": "Matt Quevedo",
    "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
  }],
  "upcoming_shows": [{
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
  }, {
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
  }, {
    "artist_id": 6,
    "artist_name": "The Wild Sax Band",
    "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
  }],
  "past_shows_count": 1,
  "upcoming_shows_count": 1,
}

# all_venue = [data1,data2,data3]

# for venue in all_venue:
#     venue = Venue(
#         #id = venue['id'],
#         name = venue['name'],
#         genres = str(venue['genres']),
#         address = venue['address'],
#         city = venue['city'],
#         state = venue['state'],
#         phone = venue['phone'],
#         website = venue['website'],
#         facebook_link = venue['facebook_link'],   
#         seeking_telent = venue['seeking_talent'],
#         seeking_description = venue['seeking_description'],
#       image_link = venue['image_link']
#     )       
#     db.session.add(venue)
#     db.session.commit()
#     db.session.close()

data1={
  "id": 4,
  "name": "Guns N Petals",
  "genres": ["Rock n Roll"],
  "city": "San Francisco",
  "state": "CA",
  "phone": "326-123-5000",
  "website": "https://www.gunsnpetalsband.com",
  "facebook_link": "https://www.facebook.com/GunsNPetals",
  "seeking_venue": True,
  "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
  "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  "past_shows": [{
    "venue_id": 1,
    "venue_name": "The Musical Hop",
    "venue_image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
    "start_time": "2019-05-21T21:30:00.000Z"
  }],
  "upcoming_shows": [],
  "past_shows_count": 1,
  "upcoming_shows_count": 0,
}
data2={
  "id": 5,
  "name": "Matt Quevedo",
  "genres": ["Jazz"],
  "city": "New York",
  "state": "NY",
  "phone": "300-400-5000",
  "website":'No Website',
  "facebook_link": "https://www.facebook.com/mattquevedo923251523",
  "seeking_venue": False,
  "seeking_description": "",
  "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  "past_shows": [{
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2019-06-15T23:00:00.000Z"
  }],
  "upcoming_shows": [],
  "past_shows_count": 1,
  "upcoming_shows_count": 0,
}
data3={
  "id": 6,
  "name": "The Wild Sax Band",
  "genres": ["Jazz", "Classical"],
  "city": "San Francisco",
  "state": "CA",
  "phone": "432-325-5432",
  "website":'No Website',
  "facebook_link": "",
  "seeking_venue": False,
  "seeking_description": "",
  "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  "past_shows": [],
  "upcoming_shows": [{
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-01T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-08T20:00:00.000Z"
  }, {
    "venue_id": 3,
    "venue_name": "Park Square Live Music & Coffee",
    "venue_image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
    "start_time": "2035-04-15T20:00:00.000Z"
  }],
  "past_shows_count": 0,
  "upcoming_shows_count": 3,
}
# all_artist = [data1,data2,data3]

# for artist in all_artist:
#     artist = Artist(
#         #id = venue['id'],
#         name = artist['name'],
#         genres = str(artist['genres']),
#         city = artist['city'],
#         state = artist['state'],
#         phone = artist['phone'],
#         website = artist['website'],
#         facebook_link = artist['facebook_link'],   
#         seeking_venue = artist['seeking_venue'],
#         seeking_description = artist['seeking_description'],
#         image_link = artist['image_link']
#     )       
#     db.session.add(artist)
#     db.session.commit()
#     db.session.close()


data=[{
  "venue_id": 1,
  "venue_name": "The Musical Hop",
  "artist_id": 4,
  "artist_name": "Guns N Petals",
  "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
  "start_time": "2019-05-21T21:30:00.000Z"
}, {
  "venue_id": 3,
  "venue_name": "Park Square Live Music & Coffee",
  "artist_id": 5,
  "artist_name": "Matt Quevedo",
  "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
  "start_time": "2019-06-15T23:00:00.000Z"
}, {
  "venue_id": 3,
  "venue_name": "Park Square Live Music & Coffee",
  "artist_id": 6,
  "artist_name": "The Wild Sax Band",
  "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  "start_time": "2035-04-01T20:00:00.000Z"
}, {
  "venue_id": 3,
  "venue_name": "Park Square Live Music & Coffee",
  "artist_id": 6,
  "artist_name": "The Wild Sax Band",
  "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  "start_time": "2035-04-08T20:00:00.000Z"
}, {
  "venue_id": 3,
  "venue_name": "Park Square Live Music & Coffee",
  "artist_id": 6,
  "artist_name": "The Wild Sax Band",
  "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
  "start_time": "2035-04-15T20:00:00.000Z"
}]

for show in data:
    show = Show(
      venue_id= show['venue_id'],
      artist_id= show['artist_id'],
      start_time= show['start_time']
    )       
    db.session.add(show)
    db.session.commit()
    db.session.close()

# venue 
# data1={
#   "id": 1,
#   "name": "The Musical Hop",
#   "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
#   "address": "1015 Folsom Street",
#   "city": "San Francisco",
#   "state": "CA",
#   "phone": "123-123-1234",
#   "website": "https://www.themusicalhop.com",
#   "facebook_link": "https://www.facebook.com/TheMusicalHop",
#   "seeking_talent": True,
#   "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
#   "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60",
#   "past_shows": [{
#     "artist_id": 4,
#     "artist_name": "Guns N Petals",
#     "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
#     "start_time": "2019-05-21T21:30:00.000Z"
#   }],
#   "upcoming_shows": [],
#   "past_shows_count": 1,
#   "upcoming_shows_count": 0,
# }
# data2={
#   "id": 2,
#   "name": "The Dueling Pianos Bar",
#   "genres": ["Classical", "R&B", "Hip-Hop"],
#   "address": "335 Delancey Street",
#   "city": "New York",
#   "state": "NY",
#   "phone": "914-003-1132",
#   "website": "https://www.theduelingpianos.com",
#   "facebook_link": "https://www.facebook.com/theduelingpianos",
#   "seeking_talent": False,
#   "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80",
#   "past_shows": [],
#   "upcoming_shows": [],
#   "past_shows_count": 0,
#   "upcoming_shows_count": 0,
# }
# data3={
#   "id": 3,
#   "name": "Park Square Live Music & Coffee",
#   "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
#   "address": "34 Whiskey Moore Ave",
#   "city": "San Francisco",
#   "state": "CA",
#   "phone": "415-000-1234",
#   "website": "https://www.parksquarelivemusicandcoffee.com",
#   "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
#   "seeking_talent": False,
#   "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80",
#   "past_shows": [{
#     "artist_id": 5,
#     "artist_name": "Matt Quevedo",
#     "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
#     "start_time": "2019-06-15T23:00:00.000Z"
#   }],
#   "upcoming_shows": [{
#     "artist_id": 6,
#     "artist_name": "The Wild Sax Band",
#     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#     "start_time": "2035-04-01T20:00:00.000Z"
#   }, {
#     "artist_id": 6,
#     "artist_name": "The Wild Sax Band",
#     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#     "start_time": "2035-04-08T20:00:00.000Z"
#   }, {
#     "artist_id": 6,
#     "artist_name": "The Wild Sax Band",
#     "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#     "start_time": "2035-04-15T20:00:00.000Z"
#   }],
#   "past_shows_count": 1,
#   "upcoming_shows_count": 1,
# }

# # artist


# data=[{
#   "venue_id": 1,
#   "venue_name": "The Musical Hop",
#   "artist_id": 4,
#   "artist_name": "Guns N Petals",
#   "artist_image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
#   "start_time": "2019-05-21T21:30:00.000Z"
# }, {
#   "venue_id": 3,
#   "venue_name": "Park Square Live Music & Coffee",
#   "artist_id": 5,
#   "artist_name": "Matt Quevedo",
#   "artist_image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
#   "start_time": "2019-06-15T23:00:00.000Z"
# }, {
#   "venue_id": 3,
#   "venue_name": "Park Square Live Music & Coffee",
#   "artist_id": 6,
#   "artist_name": "The Wild Sax Band",
#   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#   "start_time": "2035-04-01T20:00:00.000Z"
# }, {
#   "venue_id": 3,
#   "venue_name": "Park Square Live Music & Coffee",
#   "artist_id": 6,
#   "artist_name": "The Wild Sax Band",
#   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#   "start_time": "2035-04-08T20:00:00.000Z"
# }, {
#   "venue_id": 3,
#   "venue_name": "Park Square Live Music & Coffee",
#   "artist_id": 6,
#   "artist_name": "The Wild Sax Band",
#   "artist_image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
#   "start_time": "2035-04-15T20:00:00.000Z"
# }]