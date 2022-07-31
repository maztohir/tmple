from tmple.recipe import Recipe


def test_simple_var():
    recipe = Recipe({'var': {'foo': 'bar'}})
    assert recipe.var['foo'] == 'bar'


def test_var_extend():
    recipe = Recipe.from_path('samples/recipes/default.yaml')
    assert recipe.var == {'foo': 'bar', 'hello': 'world'}
