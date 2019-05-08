from TopChef.top_chef.controllers.Chefs import Chefs
from TopChef.top_chef.controllers.FormatWordScore import FormatWordScore
from TopChef.top_chef.controllers.Recipes import Recipes
from TopChef.top_chef.controllers.Reviews import Reviews
from TopChef.top_chef.models.Chef import Chef
from TopChef.top_chef.models.Recipe import Recipe
from TopChef.top_chef.models.Review import Review
import re


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
        min_raw_score=0
        max_raw_score=0
        for rev_id in self.reviews.get_ids():
            sum_score_value = self.process_review(rev_id,word_dict)
            review = self.reviews.get_review(rev_id)
            review.set_score(sum_score_value)
            if min_raw_score>review.get_score():
                min_raw_score=review.get_score()
            if max_raw_score< review.get_score():
                max_raw_score = review.get_score()
        self.normalize_reviews_scores(min_raw_score, max_raw_score)


    def process_review(self,rev_id,word_dict):
        """
        Processa cada review y le da una puntuacion por cada palabra que coincida en le diccionario
        :param rev_id:
        :param word_dict:
        :return:
        """
        review = self.reviews.get_review(rev_id)
        review_text = review.get_review()
        format = FormatWordScore(review_text)
        review_array_formated = format.format_string_score()

        score=0
        for word in review_array_formated:
            if word in word_dict.get_words():
                score+= float(word_dict.get_value(word))
        return score

    def normalize_reviews_scores(self, min_raw_score, max_raw_score):
        """
        Normaliza la puntuacion de todas las reviews.
        :param min_raw_score:
        :param max_raw_score:
        :return:
        """
        for rev_id in self.reviews.get_ids():
            self.normalize_review_score(rev_id,min_raw_score, max_raw_score)

    def normalize_review_score(self, rev_id, min_raw_score, max_raw_score):
        """
        Normaliza la puntuacion de una review
        :param rev_id:
        :param min_raw_score:
        :param max_raw_score:
        :return:
        """
        review = self.reviews.get_review(rev_id)
        rs_mRS = review.get_score() - min_raw_score
        mRS_mRS = max_raw_score - min_raw_score
        normScore = round(rs_mRS / mRS_mRS,1)
        review.set_score(normScore)

    def compute_recipes_score(self):
        # Complete this function
        for rev_id in self.reviews.get_ids():
            pass
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

