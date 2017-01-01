#! /usr/bin/env python

import os
import shutil

################################################################################
# Does damm exist?
################################################################################
damm_file = "third_party_code/damm/damm16.py"
damm_src = os.path.expanduser(
    "~/Dropbox/publicly_visible_binaries/third_party_code/damm")
damm_dst = "third_party_code/damm"

is_damm_exist_ = os.path.isfile(damm_file)
if not(is_damm_exist_):
    input("Copying damm directory okay? (return otherwise ctrl-c)" )
    shutil.copytree(damm_src, damm_dst)

################################################################################
# Does stripe exist?
################################################################################
stripe_file = "third_party_code/stripe/__init__.py"
stripe_src = os.path.expanduser(
    "~/Dropbox/publicly_visible_binaries/third_party_code/stripe")
stripe_dst = "third_party_code/stripe"
is_stripe_exist_ = os.path.isfile(stripe_file)
if not(is_stripe_exist_):
    input("Copying stripe directory okay? (return otherwise ctrl-c)")
    shutil.copytree(stripe_src, stripe_dst)
