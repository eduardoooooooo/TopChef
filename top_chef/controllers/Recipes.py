# Structure to hold the recipes
from TopChef.top_chef.Exceptions.TopChefException import TopChefException
from TopChef.top_chef.controllers.InsertionSort import InsertionSort
from TopChef.top_chef.models.Recipe import Recipe


class Recipes:
    def __init__(self):
        self.recipes = {}
        self.next_recipe = 0
        self.sorted_recipes = []

    def add_recipe(self, chef_id, name):
        self.next_recipe += 1
        new_recipe = Recipe(self.next_recipe, name, chef_id)
        self.recipes[new_recipe.get_id()] = new_recipe
        self.sorted_recipes.append(new_recipe)
        return new_recipe

    def get_ids(self):
        # Complete this function
        return list(self.recipes.keys())

    def exists(self, id):
        # Complete this function
        return id in self.recipes.keys()

    def get_recipe(self, recipe_id):
        # Complete this function
        if self.exists(recipe_id):
            return self.recipes[recipe_id]
        else:
            raise TopChefException("No existe la receta")

    def is_sorted(self):
        # Complete this function
        return False

    def sort_recipes(self):
        # Complete this function
        if self.is_sorted():
            return
        else:
            insertion_sort = InsertionSort(self.sorted_recipes)
            insertion_sort.sort()

    def get_top_n(self, n=1):
        # Complete this function
        return self.sorted_recipes[:n]

    def __str__(self):
        # Complete this function
        rec_str = ""
        return rec_str

    def __len__(self):
        # Complete this function
        return None