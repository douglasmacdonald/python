# Activate environment `py27`

See the `../README.md` at the top level for information on managing the environment.

    > source activate py27

---

# Run GAE on local machine

Running the **run_locally.sh** script in the top level GAE project directory will start the
application for development and testing. It is simply a call the the GAE
development framework, downloaded locally ~/bin/google_appengine

    > ./run_locally.sh

# app.yaml

Configuration file used by GAE. Also used here to switch between current
versions, e.g. debug, offline etc..

## Running offline

...

---


The following is deprecated while one page is being used for development.

> *Despite being able to run on your machine for development an internet connection
is still required for the payment functionality to be tested. If you want the
application to work as if payments have been successful then run the application
in ...*

---

# Local

## Setting path for local appengine

* export PATH=$PATH:/path/to/google_appengine/

# Bash script

The bash script is used to run the appengine locally.

# Stripe

## Logon

* Username: email@gmail.com
* Password: usual+ipe

## Installation

* https://pypi.python.org/pypi/stripe/1.22.2
* https://github.com/stripe/stripe-python
* https://stripe.com/docs/libraries
* https://github.com/twbs/bootstrap

## Dashboard

* https://dashboard.stripe.com/test/dashboard

## Documentation

* https://stripe.com/docs
