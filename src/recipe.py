import yaml

from .generator import Generator
from .utils import read_file
from .template import Template


class Recipe:
    def __init__(self, _dict):
        self.recipe = _dict
        self._extend_recipe = self.recipe.get('extend')
        self.var, self.func, self.generator = {}, {}, []

        if self._extend_recipe:
            self._init_extend()

        self.var.update(self.recipe.get('var', {}))
        self.func.update(self.recipe.get('func', {}))
        self.generator.extend(self.recipe.get('generator', []))

    @classmethod
    def from_path(cls, path):
        return cls(yaml.safe_load(read_file(path)))

    def _init_extend(self):
        for rec in self._extend_recipe:
            rec = Recipe.from_path(rec)
            self.var.update(rec.var)
            self.func.update(rec.func)
            self.generator.extend(rec.generator)

    def generate(self):
        for gen in self.generator:
            generator = Generator(gen)
            generator.generate(self.var)
