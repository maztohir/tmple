from .template import Template
from .utils import write_file

class Generator:

    def __init__(self, spec) -> None:
        self.template = Template.from_path(spec['template'])
        self.destination = spec.get('destination')

    def generate(self, data):
        content = self.template.render(data)
        if self.destination:
            write_file(self.destination, content)
        else:
            print(content)