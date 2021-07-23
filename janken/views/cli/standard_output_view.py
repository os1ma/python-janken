from jinja2 import Environment, FileSystemLoader

VIEW_J2_PATH = 'janken/views/cli'


class StandardOutputView:
    def __init__(self, template, params={}):
        self._template = template
        self._params = params

    def show(self):
        env = Environment(loader=FileSystemLoader(VIEW_J2_PATH))
        j2_template = env.get_template(self._template)
        print(j2_template.render(self._params))
