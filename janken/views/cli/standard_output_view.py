from jinja2 import Environment, FileSystemLoader
from typing import Dict, Any

VIEW_J2_PATH = 'janken/views/cli'


class StandardOutputView:
    def __init__(self, template: str, params: Dict[str, Any] = {}):
        self._template = template
        self._params = params

    def show(self) -> None:
        env = Environment(loader=FileSystemLoader(VIEW_J2_PATH))
        j2_template = env.get_template(self._template)
        print(j2_template.render(self._params))
