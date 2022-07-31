
import argparse
from tmple.recipe import Recipe


def main():
    args = args_parser()
    recipe = Recipe.from_path(args.recipe)
    recipe.generate()


def args_parser():
    parser = argparse.ArgumentParser(
        description='Generate a file from a template')
    parser.add_argument(
        '-r', '--recipe', help='Path to the recipes', required=True)
    return parser.parse_args()

