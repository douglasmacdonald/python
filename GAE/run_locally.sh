#!/bin/bash

# Launch a local GAE
#
# dev_appserver.py ./

source activate py27

./third_party_code_do_not_deploy/google_appengine/dev_appserver.py ./
