#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches_made = None

  for key, value in recipe.items():
    if key in ingredients.keys():
      batches_possible = ingredients[key] // value
      if batches_made is None or batches_possible < batches_made:
        batches_made = batches_possible
    else:
      batches_made = 0

  return batches_made


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))