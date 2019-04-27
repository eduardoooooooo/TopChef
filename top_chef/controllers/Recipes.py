# Structure to hold the recipes
class Recipes:
    def __init__(self):
        self.recipes = {}
        self.next_recipe = 0
        self.sorted_recipes = []

    def add_recipe(self, chef_id, name):
        # Complete this function
        return None

    def get_ids(self):
        # Complete this function
        return None

    def exists(self, id):
        # Complete this function
        return False

    def get_recipe(self, recipe_id):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_recipes(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        rec_str = ""
        return rec_str

    def __len__(self):
        # Complete this function
        return None