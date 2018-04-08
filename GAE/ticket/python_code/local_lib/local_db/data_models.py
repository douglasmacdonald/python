from google.appengine.ext import ndb

class ShowInformation(ndb.Model):
    show_id = ndb.StringProperty(indexed=False)
    title = ndb.StringProperty(indexed=False)
    image = ndb.StringProperty(indexed=False)
    website = ndb.StringProperty(indexed=False)
    facebook_text = ndb.StringProperty(indexed=False)
    facebook_web_address = ndb.StringProperty(indexed=False)
    twitter = ndb.StringProperty(indexed=False)
    short_description = ndb.StringProperty(indexed=False)
    age_restrictions = ndb.StringProperty(indexed=False)
    videos = ndb.StringProperty(indexed=False)
    comments = ndb.StringProperty(indexed=False)
    show_description = ndb.StringProperty(indexed=False)

class Price(ndb.Model):
    """Sub model for show prices."""
    short_name = ndb.StringProperty(indexed=False)
    price = ndb.StringProperty(indexed=False)
    face_value = ndb.StringProperty(indexed=False)

class PerformanceInformation(ndb.Model):
    """Sub model for representing show infomation."""
    show_id = ndb.StringProperty(indexed=False)
    date = ndb.StringProperty(indexed=False)
    doors = ndb.StringProperty(indexed=False)
    show_start = ndb.StringProperty(indexed=False)
    show_finish = ndb.StringProperty(indexed=False)
    venue = ndb.StringProperty(indexed=False)
    venue_address = ndb.StringProperty(indexed=False)
    venue_website = ndb.StringProperty(indexed=False)
    venue_phone = ndb.StringProperty(indexed=False)
    additonal_information = ndb.StringProperty(indexed=False)
    age_restrictions = ndb.StringProperty(indexed=False)
    id = ndb.StringProperty(indexed=False)
    prices = ndb.KeyProperty(kind=Price, repeated=True)
