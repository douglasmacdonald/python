'''Convenience functions relying on the os module.'''

import os

def path_to_templates_which_are_up_one_level(path_to_main
    , templates_directory_name):
    """Returns the path to the html templates."""

    templates_directory = os.path.join(path_to_main, templates_directory_name)

    path_to_templates =  [
    dirpath for dirpath, dirnames, filenames in os.walk(templates_directory)]

    return path_to_templates
