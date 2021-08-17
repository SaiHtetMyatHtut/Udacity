from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

# Show Model Creating
# Show Table is an associastion table or dummy table
class Show(db.Model):
  __tablename__ = 'Show'

  id = db.Column(db.Integer, primary_key=True)
  artist_id = db.Column(db.Integer, db.ForeignKey(
      'Artist.id'), nullable=False)
  venue_id = db.Column(db.Integer, db.ForeignKey('Venue.id'), nullable=False)
  start_time = db.Column(db.DateTime, nullable=False)

  def __repr__(self):
        return '<Show {}{}>'.format(self.artist_id, self.venue_id)

# Vanue Model Creating
class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String)
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_telent = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(300))
    image_link = db.Column(db.String(500))
    # Many to Many Relation Ship with Artist Table
    shows = db.relationship('Show',
      backref=db.backref('venue', lazy=True))

    def __repr__(self):
        return '<Venue {}>'.format(self.name)

# Artist Model Creating
class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean)
    seeking_description = db.Column(db.String(300))
    image_link = db.Column(db.String(500))
    # Many to Many Relation Ship with Venue Table
    shows = db.relationship('Show',
      backref=db.backref('artist', lazy=True))
    
    def __repr__(self):
        return '<Artist {}>'.format(self.name)
