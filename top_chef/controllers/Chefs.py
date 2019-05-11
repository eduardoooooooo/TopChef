# Structure to hold all chefs
from TopChef.top_chef.Exceptions.TopChefException import TopChefException
from TopChef.top_chef.controllers.InsertionSort import InsertionSort
from TopChef.top_chef.models.Chef import Chef


class Chefs:
    def __init__(self):
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        # Complete this function
        return id in self.chefs.keys()

    def get_ids(self):
        # Complete this function
        return list(self.chefs.keys())

    def add_chef(self, name, restaurant):
        self.next += 1
        new_chef = Chef(self.next, name, restaurant)
        self.chefs[new_chef.get_id()] = new_chef
        self.sorted_chefs.append(new_chef)
        return new_chef

    def get_chef(self, id):
        # Complete this function
        if self.exists(id):
            return self.chefs[id]
        else:
            raise TopChefException("El chef no existe")

    def is_sorted(self):
        # Complete this function
        return False

    def sort_chefs(self):
        # Complete this function
        insertion_sort = InsertionSort(self.sorted_chefs)
        insertion_sort.sort()

    def get_top_n(self, n=1):
        # Complete this function
        return self.sorted_chefs[:n]

    def __str__(self):
        # Complete this function
        chefs_str = ""
        return chefs_str

    def __len__(self):
        # Complete this function
        return None