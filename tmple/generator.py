from .template import Template
from .utils import write_file


class Generator:

    def __init__(self, spec) -> None:
        self.template = Template.from_path(spec['template'])
        self.destination = spec.get('destination')

    def generate(self, data):
        content = self.template.render(data)

        if isinstance(self.destination, list):
            for dest in self.destination:
                self.write(dest, content)

        elif isinstance(self.destination, str):
            self.write(self.destination, content)

        else:
            print(content)

    def write(self, path, content):
        if path is None and content is None:
            raise ValueError('Both path and content are None')

        if path == 'log':
            print(content)
        else:
            write_file(path, content, create_if_folder_not_found=True)
