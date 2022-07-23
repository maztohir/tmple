from src.recipe import Recipe

recipe = Recipe('samples/recipes/simple.yaml')


def test_var():
    assert recipe.var == {'data': 'halo',  'foo': 'bar', 'hello': 'world'}
