# TODO

* http://kawahara.ca/using-numpy-on-google-app-engine-with-the-anaconda-python-distribution/

---

# When reading this using Atom

To preview this `README.md` rendered markdown.

    ctrl-shift-m

---

# Purpose and organisation

* This directory tree contains GAE projects.
* Individual GAE projects are under there own directory.
* Code is not shared directly between these and are there own environment.
* Projects only using the GAE standard environment. https://cloud.google.com/appengine/docs/the-appengine-environments
 * In the future, if we start using `GAE`'s `flexible` environment then change the organisation of the directory tree, thus:


    GAE+
       |
       +-flexible
       |
       +-standard

# Set-up

* Anaconda
 * For development only, using the Anaconda Python distribution.
 * Install the latest `Anaconda` `Python 3.x`.
 * `GAE` uses `Python 2.7`. However, I now mainly use `Python 3.x` and use the `Python` `Anaconda` distribution to manage the environments to switch to 2.7

# Environment

Switching between versions of Python

http://conda.pydata.org/docs/py2or3.html

## Environment - creating

* https://conda.io/docs/user-guide/tasks/manage-python.html
* `conda create -n py27 python=2.7 anaconda`

##  Look for avaialble verions

    $ conda search python | less

## Environment - activation

To activate this environment, use:

`> source activate py27`

To deactivate an active environment, use:

`> source deactivate`

`> source deactivate py27`

# GAE

## GAE - download

* https://cloud.google.com/appengine/downloads
* https://cloud.google.com/appengine/docs/standard/python/download

## GAE - setup

`./google-cloud-sdk/bin/gcloud init`

## Original GAE

For downloading existing code, original `GAE` required.

# Download our code already deployed on GAE

`~/google_appengine$ ./appcfg.py download_app -A zombie-science-exams-d -V 3`

`~/git/python/GAE/zombie_exams/`
