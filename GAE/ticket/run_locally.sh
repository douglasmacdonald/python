#!/bin/bash

# Launch a local GAE
#
# dev_appserver.py ./

# This part is done in Python 3.x 
./python_code/check_third_party_code.py

source activate py27

#./third_party_code_do_not_deploy/google_appengine/dev_appserver.py ./
~/Dropbox/publicly_visible_binaries/third_party_code_do_not_deploy/google_appengine/dev_appserver.py ./
