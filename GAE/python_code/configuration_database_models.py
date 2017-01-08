################################################################################
# TICKET INFORMATION PROVIDED BY SHOW ORGANISORS
################################################################################
""" Information that vendor provides concerning products and prices etc. In the
future, this function will be replaced with some form of database etc. For
development, this contains show and ticket information. In the future this will
be provided by a database."""


#https://cloud.google.com/appengine/docs/python/getting-started/storing-data-datastore
#https://cloud.google.com/appengine/docs/python/ndb/creating-entities
#https://cloud.google.com/appengine/docs/python/ndb/entity-property-reference
#https://cloud.google.com/appengine/docs/python/datastore/typesandpropertyclasses
#https://cloud.google.com/appengine/docs/python/datastore/datamodeling#Lists
#https://cloud.google.com/appengine/articles/modeling
#https://cloud.google.com/appengine/docs/python/ndb/entity-property-reference#structured


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

show_information_entry = ShowInformation(show_id = "gotd"
    , title = "Zombie Science: Genes of the Damned")

show_information_entry.put()


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

performance_information_entry = PerformanceInformation(show_id = 'gotd'
    , date =  'Sat 12 Mar'
    , doors = '18:00'
    , show_start = '18:30'
    , show_finish = '19:45'
    , venue = "DRAM!, Glasgow"
    , venue_address = "232-246 Woodlands Road, Glasgow, G3 6ND"
    , venue_website = "https://www.facebook.com/dramglasgow/"
    , venue_phone = "0141 332 1622"
    , additonal_information = ""
    , age_restrictions = "This event is for over 18s only - No refunds will be issued for under 18s."
    , id = "1"
    , prices = [
        Price(short_name = "Concession"
            , price = "3.00"
            , face_value = "3.30").put()
        , Price(short_name = "General"
            , price = "5.50"
            , face_value = "5.00").put()
        ]
    )

performance_information_entry.put()
