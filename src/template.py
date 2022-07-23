import jinja2

from .utils import read_file


class Template:
    def __init__(self, _str):
        self.template = _str

    @classmethod
    def from_path(cls, path):
        return cls(read_file(path))

    def render(self, data, keep_trailing_newline=True):
        template = jinja2.Template(
            self.template, keep_trailing_newline=keep_trailing_newline)
        return template.render(**data)
