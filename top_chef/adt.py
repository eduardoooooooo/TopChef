class TopChefException(Exception):
    pass

#  Structure to hold a chef
class Chef:
    def __init__(self, chef_id=None, chef_name=None, chef_restaurant=None):
        self.id = chef_id
        self.name = chef_name
        self.restaurant = chef_restaurant
        self.score = 0.0

    def get_id(self):
        return self.id

    def add_score(self, score):
        self.score += score

    def get_name(self):
        return self.name

    def get_restaurant(self):
        return self.restaurant

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        chef_str = "ID: %s; " % (str(self.id))
        chef_str += "NAME: %s; " % (self.name)
        chef_str += "RESTAURANT: %s; " % (self.restaurant)
        chef_str += "SCORE: %s" % (self.score)
        return chef_str

# Structure to hold all chefs
class Chefs:
    def __init__(self):
        self.chefs = {}
        self.next = 0
        self.sorted_chefs = []

    def exists(self, id):
        # Complete this function
        return False

    def get_ids(self):
        """
        Devuelve los ids de los chefs que hay

        :return ids: (list) Ids de los chefs
        """
        # Complete this function
        ids = []

        return ids

    def add_chef(self, name, restaurant):
        """
        Crea y añade al diccionario la clase "Chef"que contiene el nombre del Chef y el restaurante en el que trabaja
        Lo añade también a "self.sorted_chefs" y lo ordena.
        
        :param name:        (String)    Nombre del chef
        :param restaurant:  (String)    Restaurante en el que trabaja
        """
        # Complete this function
        self.next += 1
        chef = Chef(self.next, name, restaurant)
        self.chefs[self.next] = chef
        self.sorted_chefs.append(chef)
        if not self.is_sorted():
            self.sort_chefs()
        return None

    def get_chef(self, id):
        """
        Devuelve el objeto/clase "Chef"

        :param id:      (Integer)   Id del chef
        :return chef:   (Object)    Clase "Chef"
        """
        # Complete this function
        chef = self.chefs.get(id)
        return chef

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

# Structure to hold a recipe
class Recipe:
    def __init__(self, rec_id=None, rec_name=None, rec_chef_id=None):
        self.id = rec_id
        self.name = rec_name
        self.chef_id = rec_chef_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def add_score(self, score):
        self.score += score

    def get_chef_id(self):
        return self.chef_id

    def __str__(self):
        rec_str = "ID: %s; " % (str(self.id))
        rec_str += "NAME: %s; " % (self.name)
        rec_str += "CHEF ID: %s; " % (self.chef_id)
        rec_str += "SCORE: %s" % (self.score)
        return rec_str

# Structure to hold the recipes
class Recipes:
    def __init__(self):
        self.recipes = {}
        self.next_recipe = 0
        self.sorted_recipes = []

    def add_recipe(self, chef_id, name):
        """
        Crea y añade al diccionario la clase "Recipe"que contiene la reseña con el id del chef
        Lo añade también a "self.sorted_recipes" y lo ordena.
        
        :param chef_id: (Integer)   Id del chef
        :param name:    (String)    Nombre de la receta 
        """
        # Complete this function
        self.next_recipe += 1
        recipe = Recipe(self.next_recipe, name, chef_id)
        self.recipes[self.next_recipe] = recipe
        self.sorted_recipes.append(recipe)
        self.sort_recipes()
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

# Structure to hold a review
class Review:
    def __init__(self, rev_id=None, review=None, rec_id=None):
        self.id = rev_id
        self.review = review
        self.recipe_id = rec_id
        self.score = 0.0

    def get_id(self):
        return self.id

    def get_review(self):
        return self.review

    def get_recipe_id(self):
        return self.recipe_id

    def get_score(self):
        return self.score

    def set_score(self, score):
        self.score = score

    def __str__(self):
        recipe_str = "ID: %s; " % (str(self.id))
        recipe_str += "REVIEW: %s; " % (self.review)
        recipe_str += "RECIPE ID: %s; " % (self.recipe_id)
        recipe_str += "SCORE: %s" % (self.score)
        return recipe_str

# Structure to hold the reviews
class Reviews:
    def __init__(self):
        self.reviews = {}
        self.next_review = 0
        self.sorted_reviews = []

    def add_review(self, rec_id, review):
        """
        Crea y añade al diccionario la clase "Review"que contiene la reseña con el id de la receta
        Lo añade también a "self.sorted_reviews" y lo ordena.

        :param rec_id: (Integer)    Id de la receta
        :param review: (String)     Reseña 
        """
        # Complete this function
        self.next_review += 1
        review = Review(self.next_review, review, rec_id)
        self.reviews[self.next_review] = review
        self.sorted_reviews.append(review)
        self.sort_reviews()
        return None

    def get_ids(self):
        # Complete this function
        return None

    def exists(self, id):
        # Complete this function
        return False

    def get_review(self,rev_id):
        # Complete this function
        return None

    def min_score(self):
        # Complete this function
        return None

    def max_score(self):
        # Complete this function
        return None

    def is_sorted(self):
        # Complete this function
        return False

    def sort_reviews(self):
        # Complete this function
        pass

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        rev_str = ""
        return rev_str


class TopChef:

    def __init__(self):
        self.chefs = Chefs()
        self.recipes = Recipes()
        self.reviews = Reviews()

    def load_data(self, path):
        # Complete this function
        """
        Lee el "path" dado con la estructura predeterminada y crea los chef con sus platos y
        reviews correspondientes, raise TopChefException en caso de que no tenga el formato
        deseado y reiniciamos la database para que no contenga información ya cargada.

        :param path: (Object) Fichero que contiene los datos
        """
        CHEF_CHAR = "CHEF"
        COURSE_CHAR = "COURSE"
        TAB = "\t"

        with open(path) as f:
            line = f.readline()
            while line != "":
                if (CHEF_CHAR or TAB) not in line:
                    raise TopChefException('Wrong file')
                # siempre tendra "CHEF ..." y lo convierte en una lista
                chef_line_list = line.split(TAB)
                try:
                    header, name, restaurant = chef_line_list
                    self.add_chef(name, restaurant)
                except ValueError:
                    self.clear()
                    raise TopChefException('Wrong TopChef Data File')
                # siguiente linea
                line = f.readline()

                while (CHEF_CHAR not in line) and (COURSE_CHAR in line) and line != "":
                    # siempre empezará "COURSE ..."
                    course_line_list = line.split(TAB)
                    header, recipe_name = course_line_list
                    self.add_recipe(self.chefs.next, recipe_name) 

                    line = f.readline()   
                    while (CHEF_CHAR not in line) and (COURSE_CHAR not in line) and line != "":
                        self.add_review(self.recipes.next_recipe, line)
                        line = f.readline()

    def clear(self):
        # Complete this function
        """
        Reinicia toda la database en caso de que hubiera una carga de la base de datos erronea para
        que no contenga la información ya añadida.
        """
        self.__init__()

    def add_chef(self, name, rest):
        """
        Llama al método add_chef de la clase self.chefs para añadir un nuevo chef a la clase.
        
        :param name: (String) Nombre del chef
        :param rest: (String) Restaurante del chef
        """
        # Complete this function
        self.chefs.add_chef(name, rest)
        return None

    def add_recipe(self, id_chef, name):
        """
        Llama al método add_recipe de la clase self.recipes para añadir una nueva receta con la
        id del chef.

        :param id_chef: (Integer)   El id del chef
        :param name:    (String)    Nombre de la receta:
        """
        # Complete this function
        self.recipes.add_recipe(id_chef,name)
        return None

    def add_review(self, id_rev,review):
        """
        Llama al método add_review de la clase self.reviews para añadir una nueva reseña con el
        id de la receta.
        
        :param id_rev: (Integer)    id de la receta
        :param review: (String)     la reseña 
        """
        # Complete this function
        self.reviews.add_review(id_rev, review)
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