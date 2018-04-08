import jinja2


class TemplateWrapper:
    def __init__(self, template):
        self.template = template

    def render(self, template_variables):
        return self.template.render(template_variables)

class TemplateEnvironmentWrapper:
    "Wrapper to only expose selected methods, Reducing test interface"
    def __init__(self, te):
        self.te = te

    def get_template(self, template_file_name):
        return TemplateWrapper(self.te.get_template(template_file_name))

def get_jinja_environment(path_to_templates):
    """ Function groups the code of generating the Jinja environment."""

    jinja_environment = jinja2.Environment(
        loader = jinja2.FileSystemLoader(path_to_templates),
        extensions = ['jinja2.ext.autoescape'],
        autoescape = True)

    return jinja_environment

def get_template_environment(path_to_templates):    

    return TemplateEnvironmentWrapper(get_jinja_environment(path_to_templates))

