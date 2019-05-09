# Structure to hold all chefs
from TopChef.top_chef.models.Chef import Chef


class Chefs:
    def __init__(self):
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        # Complete this function
        return False

    def get_ids(self):
        # Complete this function
        return list(self.chefs.keys())

    def add_chef(self, name, restaurant):
        self.next += 1
        new_chef = Chef(self.next, name, restaurant)
        self.chefs[new_chef.get_id()] = new_chef

        return new_chef

    def get_chef(self, id):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_chefs(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        chefs_str = ""
        return chefs_str

    def __len__(self):
        # Complete this function
        return None