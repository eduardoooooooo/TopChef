from TopChef.top_chef.controllers.Chefs import Chefs
from TopChef.top_chef.controllers.Recipes import Recipes
from TopChef.top_chef.controllers.Reviews import Reviews


class TopChef:

    def __init__(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        # Complete this function
        pass

    def clear(self):
        # Complete this function
        pass

    def add_chef(self, name, rest):
        # Complete this function
        return None

    def add_recipe(self, id_chef, name):
        # Complete this function
        return None

    def add_review(self, id_rev,review):
        # Complete this function
        return None

    def compute_scores(self, word_dict):
        self.compute_reviews_score(word_dict)
        self.compute_recipes_score()
        self.compute_chefs_score()

    def compute_reviews_score(self, word_dict):
        # Complete this function

        for rev_id in self.reviews.get_ids():
            continue

        self.normalize_reviews_scores()

    def normalize_reviews_scores(self):
        # Complete this function
        pass

    def compute_recipes_score(self):
        # Complete this function
        for rev_id in self.reviews.get_ids():
            continue
        self.normalize_recipes_scores()

    def normalize_recipes_scores(self):
        # Complete this function
        pass

    def compute_chefs_score(self):
        # Complete this function
        for rec_id in self.recipes.get_ids():
            continue

    def normalize_chefs_scores(self):
        # Complete this function
        pass

    def sort_structures(self):
        self.chefs.sort_chefs()
        self.recipes.sort_recipes()
        self.reviews.sort_reviews()

    def get_top_n_chefs(self, n=1):
        # Complete this function
        return None

    def get_top_n_recipes(self, n=1):
        # Complete this function
        return None

    def get_top_n_reviews(self, n=1):
        # Complete this function
        return None

    def show_chefs(self, chefs):
        # Complete this function
        pass

    def show_recipes(self, recipes):
        # Complete this function
        pass

    def show_reviews(self, reviews):
        # Complete this function
        pass