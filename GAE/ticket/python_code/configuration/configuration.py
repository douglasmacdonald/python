#-*- coding: utf-8 -*-
"""
This is general configuration for the whole application.

NOTE: much of this configuration is for development and debugging. In the future
this will be broken up and repaced with data base and user input configuration.
"""

import local_lib.local_db.data_models as data_models

################################################################################
#
################################################################################
default_payment_details_dictionaries = {
'test' : {
            'default_card_number' : "4242424242424242",
            'default_cvc' : "123",
            'default_expiration_month' : "12",
            'default_expiration_year' : "2017",
            'default_amount' : "123.45",
            'default_name' : "J SMITH",
            'default_currency' : "gbp",
            'default_description' : "Testing payment",
           },

'empty' : {
            'default_card_number': "",
            'default_cvc': "",
            'default_expiration_month': "",
            'default_expiration_year': "",
            'default_amount': "",
            'default_name': "",
            'default_currency': "",
            'default_description' : "",
           }
}

"""Configuration for Stripe payments"""

# Set your secret key: remember to change this to your live secret key in
# production.
# See your keys here https://dashboard.stripe.com/account/apikeys
_stripe_api_key = "sk_test_UUH9bzEg6OV6HOhkfECvfJdX"
payment_provider_api_key = _stripe_api_key

# Stripe requires, for example, pounds and dollars to be converted into pence
# and cents. In the future, this will have to be done dynamically depending on
# the currency.
multiplier_to_minor_currency_unit = 100

# The configuration for the pay page.
default_payment_details = "test"

_stripe_publishable_key = "pk_test_QoFdqP4bCXiGXkwHA1Nw8JmN"

publishable_key = _stripe_publishable_key

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

show_information_entry = data_models.ShowInformation(show_id = "gotd"
    , title = "Zombie Science: Genes of the Damned")

show_information_entry.put()

show_information = {

    'gotd':{
        'show_id': "gotd",
        'title': "Zombie Science: Genes of the Damned",
        'image': '',
        'website': 'www.zombiescience.co.uk',
        'facebook_text': "Zombie Science on Facebook",
        'facebook_web_address': 'https://www.facebook.com/zombiescience',
        'twitter': '@ZombieScience1Z',
        'short_description': "A spoof lecture exploring the science of a Zombieism outbreak. How will you deal with the damned?",
        'age_restrictions': "This event is for over 18s only - No refunds will be issued for under 18s.",
        'videos': "",
        'comments': "",
        'show_description': "In this lecture, theoretical Zombiologist Dr. Smith asks whether you know what to do when the Zombie Apocalypse occurs and you find yourself in your own real-life zombie horror film. See the  lessons we can learn from disease outbreaks through history, discover what genetic and social factors could affect susceptibility to Zombieism and find out how modern medical technology such as stem cell  technology could be used to help the survivors. The outcome of the show will be decided by the audience - how will you deal with the Damned?",
    },

    'wcs':{
       'show_id': "wcs"
       , 'title': "Worst Case Senario"
       , 'short_description': "..."
    },

    'another':{
       'show_id': "another",
       'title': "Another show",
       'short_description': "This is another show"
    }

    }

performance_information_entry = data_models.PerformanceInformation(show_id = 'gotd'
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
        data_models.Price(short_name = "Concession"
            , price = "3.00"
            , face_value = "3.30").put()
        , data_models.Price(short_name = "General"
            , price = "5.50"
            , face_value = "5.00").put()
        ]
    )

performance_information_entry.put()

# Data base of all performances, including past, current and future.
performance_dic = {
    'gotd':[{
        'show_id': 'gotd',
        'date': "Sat 12 Mar",
        'doors': "18:00",
        'show_start':"18:30",
        'show_finish': "19:45",
        'admission_price':[
            {
                'short_name': "General",
                'price': "5.50",
                'general_admission_face_value': "5.00",
            },
            {
                'short_name': "Concession",
                'concession_admission_face_value': "3.00",
                'price': "3.30",
            }],
        'venue': "DRAM!, Glasgow",
        'venue_address': "232-246 Woodlands Road, Glasgow, G3 6ND",
        'venue_website': "https://www.facebook.com/dramglasgow/",
        'venue_phone': "0141 332 1622",
        'additonal_information': "",
        'age_restrictions': "This event is for over 18s only - No refunds will be issued for under 18s.",
        'id': "1"
        },
        {
        'show_id': 'gotd',
        'date': "Sat 19 Mar",
        'doors': "",
        'show_start':"19:00",
        'show_finish': "",
        'admission_price':[
            {
                'short_name': "General",
                'price': "15.50",
                'general_admission_face_value': "15.00",
            },
            {
                'short_name': "Concession",
                'concession_admission_face_value': "13.00",
                'price': "13.30",
            }],
        'venue': "The Iron Horse, Glasgow",
        'venue_address': "115 West Nile Street, Glasgow, G1 2SB",
        'venue_website': "",
        'venue_phone': "0141 332 2215",
        'additional_information': "Part of British Science Week.",
        'age_restrictions': "This event is for over 18s only - No refunds will be issued for under 18s.",
        'id': "2"}],
         }

#import pandas as pd
#show_performance_information_df = pd.read_csv('../database/show_performance_information.csv')

#List of currently available shows.
product_id_dic = {
    '1':performance_dic['gotd'][0],
    '2':performance_dic['gotd'][1]}

#Adding the list of available performances to the show information.
show_information['gotd']['performances'] = performance_dic['gotd']

shows_list = [show_information['gotd']
    , show_information['wcs']
    , show_information['another']]
