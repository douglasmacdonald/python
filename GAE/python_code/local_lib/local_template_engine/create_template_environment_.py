from local_lib.local_os.path_to_templates import path_to_templates_which_are_up_one_level
from local_lib.local_sys.path_to_main import path_to_main

def create_template_environment(template_engine, path_to_templates_in):

    template_environment = template_engine.get_template_environment(
        path_to_templates_in) 
 
    return template_environment

def create_template_environment_walk(template_engine, path_to_templates_in):

    path_to_templates = path_to_templates_which_are_up_one_level(
        path_to_main(), path_to_templates)

    template_environment = template_engine.get_template_environment(
        path_to_templates) 

    return template_environment
