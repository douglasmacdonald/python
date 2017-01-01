from google.appengine.ext import ndb

#TODO: decouple the particular database.
# Or this could be moved out of the local code.

class Ticket(ndb.Model):
    """Ticket data base model."""
    number = ndb.StringProperty(indexed=False)
    name_on_ticket = ndb.StringProperty(indexed=True)
    date_time_entered = ndb.DateTimeProperty(auto_now_add=True, indexed=True)

def append(ticket_number, name_on_ticket, total_cost):

    ticket = Ticket(number = ticket_number, name_on_ticket = name_on_ticket)
    key = ticket.put()

    return key  

def get_ticket_list_sorted(sort_by):

    ticket_query = Ticket.query()
    ticket_query = ticket_query.order(sort_by)
    tickets_list = ticket_query.fetch()

    return tickets_list

def get_ticket_list():

    return get_ticket_list_sorted(-Ticket.date_time_entered)

