Using atom. To preview.

`ctrl-shift-m`

* This directory contains GAE projects.
* Individual projects are under there own directory.
* Code is not shared directly between these and are there own environment.
* Currently only using the GAE standard environment. https://cloud.google.com/appengine/docs/the-appengine-environments
 * When we start using `flexible` then the directory structure should change


    GAE+
       |
       +-flexible
       |
       +-standard

# Installation

* https://conda.io/docs/user-guide/tasks/manage-python.html
* `conda create -n py27 python=2.7 anaconda`

To activate this environment, use:
` > source activate py27`

To deactivate an active environment, use:
`> source deactivate`


GAE

source activate py27

* I tend to work with Anaconda Python 3
* http://kawahara.ca/using-numpy-on-google-app-engine-with-the-anaconda-python-distribution/
* https://cloud.google.com/appengine/downloads
* https://cloud.google.com/appengine/docs/standard/python/download

`./google-cloud-sdk/bin/gcloud init`

Also need original app engine.

Download code.

~/google_appengine$ ./appcfg.py download_app -A zombie-science-exams-d -V 3 ~/git/python/GAE/zombie_exams/
