from TopChef.top_chef.controllers.Chefs import Chefs
from TopChef.top_chef.controllers.Recipes import Recipes
from TopChef.top_chef.controllers.Reviews import Reviews
from TopChef.top_chef.models.Chef import Chef
from TopChef.top_chef.models.Recipe import Recipe
from TopChef.top_chef.models.Review import Review


class TopChef:

    def __init__(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        # Complete this function
        top_chef = open(path,"r")
        top_chef_line = top_chef.readline().split("\t")
        while top_chef_line[0]!="":
            self.process_line(top_chef_line)
            top_chef_line = top_chef.readline().split("\t")



    def process_line(self,data):
        """
        Devuelve el objeto correspondiente dependiendo de la primera palabra de la linea
        :param data: Array donde cada componente se consigue haciendo un split usando como referencia el tabulador de una linea
        :return: Un objeto dependiendo de la primera palabra del array (Chef,Recipe,Review)
        """
        if data[0] == "CHEF":
            new_chef = self.add_chef(data[1],data[2].replace("\n",""))
            return new_chef
        elif data[0] == "COURSE":
            id_last_chef = self.chefs.next - 1
            new_recipe = self.add_recipe(id_last_chef,data[1].replace("\n",""))
            return new_recipe
        else:
            id_last_recipe = self.recipes.next_recipe - 1
            new_review = self.add_review(id_last_recipe,data[0].replace("\n",""))
            return new_review

    def clear(self):
        # Complete this function
        pass

    def add_chef(self, name, rest):
        return self.chefs.add_chef(name,rest)


    def add_recipe(self, id_chef, name):
        return self.recipes.add_recipe(id_chef,name)

    #id_rev --> id_rec debido a que se pasa el id de la recete no el del id
    def add_review(self, id_rec, review):
        return self.reviews.add_review(id_rec,review)

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
