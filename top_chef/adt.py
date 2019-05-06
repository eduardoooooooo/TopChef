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

        :return ids: (List) Ids de los chefs
        """
        # Complete this function
        ids = []
        for key in self.chefs:
            ids.append(key)

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
        """
        Mira dentro de la lista "self.sorted_chefs" cogiendo cada clase y compara sus scores.

        :return: (Boolean)  False si no esta ordenado y True si esta ordenado
        """
        # Complete this function
        sort = True
        if len(self.sorted_chefs) > 1:
            for i in range(len(self.sorted_chefs)-1):
                score_1 = self.sorted_chefs[i].score
                score_2 = self.sorted_chefs[i+1].score
                if score_1 < score_2:
                    sort = False
        return sort

    def sort_chefs(self):
        """
        Ordena la lista "self.sorted_chefs" de mayor a menor de los scores

        :return: None
        """
        # Complete this function
        for i in range(len(self.sorted_chefs)-1):
            i += 1
            j = i
            # j para marcar el limite de la lista, que el score anterior no sea menor que el actual
            while j > 0 and self.sorted_chefs[j].score > self.sorted_chefs[j-1].score:
                chef_1 = self.sorted_chefs[j]
                chef_2 = self.sorted_chefs[j-1]
                self.sorted_chefs[j] = chef_2
                self.sorted_chefs[j-1] = chef_1
                j -= 1

    def get_top_n(self, n=1):
        """
        Devuelve una lista con los top n que se le pasa como parametro.

        :param n:           (Integer)   La cantidad de los mejores n chefs
        :return top_chefs:  (List)      Lista de los mejores n chefs
        """
        # Complete this function
        lista = self.sorted_chefs[:n]
        return lista

    def __str__(self):
        # Complete this function
        chefs_str = "######\tChefs\t######\n"
        for chef in self.sorted_chefs:
            chefs_str += str(chef)
            chefs_str += "\n"
        return chefs_str

    def __len__(self):
        """
        Cantidad de chefs que hay en la clase
        
        :return: (Integer)  Cantidad de chefs
        """
        # Complete this function
        return len(self.sorted_chefs)

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
        #return None

    def get_ids(self):
        """
        Devuelve los ids que haya en el diccionario en forma de lista

        :return ids: (List) Lista de ids
        """
        # Complete this function
        ids = []
        for key in self.recipes:
            ids.append(key)
        return ids

    def exists(self, id):
        # Complete this function
        return False

    def get_recipe(self, recipe_id):
        """
        Devuelve el objeto que le corresponde a la id proporcionada.

        :param recipe_id:   (Integer)   Id de la receta
        :return:            (Object)    Objeto con dicha id
        """
        # Complete this function
        return self.recipes.get(recipe_id)

    def is_sorted(self):
        """
        Comprueba si el atributo "self.sorted_recipes" esta ordenado

        :return: (Boolean)  True si esta ordenado / False si esta desordenado
        """
        # Complete this function
        sort = True
        if len(self.sorted_recipes) > 1:
            for i in range(len(self.sorted_recipes)-1):
                score_1 = self.sorted_recipes[i].score
                score_2 = self.sorted_recipes[i+1].score
                if score_1 < score_2:
                    sort = False
        return sort

    def sort_recipes(self):
        """
        Ordena la lista "self.sorted_recipes"

        :return: None
        """
        # Complete this function
        for i in range(len(self.sorted_recipes)-1):
            i += 1
            j = i
            
            # j para marcar el limite de la lista, y que actual < anterior
            while j > 0 and self.sorted_recipes[j].score > self.sorted_recipes[j-1].score:
                recipe_1 = self.sorted_recipes[j]
                recipe_2 = self.sorted_recipes[j-1]
                self.sorted_recipes[j] = recipe_2
                self.sorted_recipes[j-1] = recipe_1
                j -= 1

    def get_top_n(self, n=1):
        """
        Devuelve una lista de los mejores n chefs

        :param n:      (Integer)    Cantidad de las mejores recetas
        :return lista: (List)       Lista de las mejores n recetas
        """
        # Complete this function
        lista = self.sorted_recipes[:n]
        return lista

    def __str__(self):
        # Complete this function
        rec_str = "######\tRecipes\t######\n"
        for rec in self.sort_recipes:
            rec_str += str(rec)
            rec_str += "\n"

        return rec_str

    def __len__(self):
        """
        Cantidad de recetas en la clase

        :return: (Integer)  Numero de recetas
        """
        # Complete this function
        return len(self.sorted_recipes)

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
        self.reviews =  {}
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

    def get_ids(self):
        """
        Añade a una lista las claves que son los ids de los reviews del diccionario.

        :return: (Lista)    Devuelve la lista de los ids de los reviews
        """
        # Complete this function
        lista = []
        for key in self.reviews:
            lista.append(key)
        return lista

    def exists(self, id):
        # Complete this function
        return False

    def get_review(self,rev_id):
        # Complete this function
        return self.reviews.get(rev_id)

    def min_score(self):
        """
        Devuelve el ultimo que se encuentra en la lista "self.sorted_reviews"

        :return: (Float)    El score del ultimo review que es el minimo
        """
        # Complete this function
        return self.sorted_reviews[-1].score

    def max_score(self):
        """
        Devuelve el primero que se encuentra en la lista "self.sorted_reviews:

        :return: (Float)    El score del primer review que es el maximo
        """
        # Complete this function
        return self.sorted_reviews[0].score

    def is_sorted(self):
        """
        Comprueba si la lista de "self.sorted_reviews" esta ordenado

        :return: (Boolean)  False si no esta ordenado / True si esta ordenado
        """
        # Complete this function
        sort = True
        if len(self.sorted_reviews) > 1:
            for i in range(len(self.sorted_reviews)-1):
                score_1 = self.sorted_reviews[i].score
                score_2 = self.sorted_reviews[i+1].score
                if score_1 > score_2:
                    sort = False
        return sort

    def sort_reviews(self):
        """
        Ordena la lista "self.sorted_reviews" de mayor a menor de los scores de cada review.

        :return: None
        """
        # Complete this function
        for i in range(len(self.sorted_reviews)-1):
            i += 1
            j = i

            # mientras que j no sea 0 (si es 0 es que ha llegado al final) y que el score anterior no sea mayor no parara
            while j > 0 and  self.sorted_reviews[j].score > self.sorted_reviews[j-1].score:
                review_1 = self.sorted_reviews[j]
                review_2 = self.sorted_reviews[j-1]
                self.sorted_reviews[j] = review_2
                self.sorted_reviews[j-1] = review_1
                j -= 1

    def get_top_n(self, n=1):
        """
        Lista de los mejores n reviews

        :return lista: (List)   Mejores n reviews
        """
        # Complete this function
        lista = self.sorted_reviews[:n]
        return lista

    def __str__(self):
        """
        Devuelve un string que contiene la informacion de todos los reviews ordanados

        :return rev_str:    (String)    Informacion de todos los reviews
        """
        # Complete this function
        rev_str = "######\tReviews\t###### \n"
        for review in self.sorted_reviews:
            rev_str += str(review)
            rev_str += "\n"

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

        # reiniciamos la clase por si habia datos anteriores
        self.clean()

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
        """
        Calcula la nota apartir de un diccionario de palabras el cual le corresponde una puntuacion.
        La nota es la suma de estas puntuaciones

        :param word_dict: (Object)  Es una clase que contiene un diccionario el cual la clave es la palabra
                                        y el valor es la puntuacion. 
        """
        # Complete this function

        DOT = '.'
        COMMA = ','
        NOTHING = ''
        for rev_id in self.reviews.get_ids():
            review_obj = self.reviews.get_review(rev_id)
            review = review_obj.get_review()
            # lo convertirmos en minúscula todo
            review = review.lower()
            # eliminamos los '.' y ','
            review = review.replace(DOT, NOTHING).replace(COMMA, NOTHING)
            lista = review.split()
            score = 0
            for word in lista:
                if word_dict.exists(word):
                    score += word_dict.get_value(word)
            review_obj.set_score(score)

        self.normalize_reviews_scores()

    def normalize_reviews_scores(self):
        """
        Normaliza los scores de todos los reviews
        """
        # Complete this function
        max_score = self.reviews.max_score()
        min_score = self.reviews.min_score()
        id_list = self.reviews.get_ids()
        for id in id_list:
            review = self.reviews.get_review(id)
            raw_score = review.get_score()
            norm_score = (raw_score-min_score)/(max_score-min_score)
            review.score = norm_score

    def compute_recipes_score(self):
        """
        Calcula la media aritmetica de las reviews que le corresponden a cada receta.
        """
        # Complete this function
        rev_ids = self.reviews.get_ids()
        for rec_id in self.recipes.get_ids():   #####cambio de recipes en vez de reviews
            # clase recipe
            recipe = self.recipes.get_recipe(rec_id)
            counter = 0
            # busca en todos los reviews
            for rev_id in rev_ids:
                review = self.reviews.get_review(rev_id)
                # mira si coincide el id de la receta 'en' la review y de la id de la receta
                if review.get_id() == rec_id:
                    recipe.add_score(review.get_score())
                    counter += 1

            recipe_score = recipe.get_score()
            # hace la media del score
            try:
                recipe.set_score(recipe_score/counter)
            except ZeroDivisionError:
                continue

        self.normalize_recipes_scores()

    def normalize_recipes_scores(self):
        """
        Normaliza los scores de las recetas
        """
        # Complete this function
        max_score = self.recipes.get_top_n(-1)[0].get_score()
        min_score = self.recipes.get_top_n(1)[0].get_score()
        id_list = self.recipes.get_ids()
        for id in id_list:
            recipe = self.recipes.get_recipe(id)
            raw_score = recipe.get_score()
            try:
                norm_score = (raw_score-min_score)/(max_score-min_score)
                recipe.score = norm_score
            except ZeroDivisionError:
                continue

    def compute_chefs_score(self):
        # Complete this function
        rec_ids = self.recipes.get_ids()
        for chef_id in self.chefs.get_ids():   #####cambio de recipes en vez de reviews
            # clase recipe
            chef = self.chefs.get_chef(chef_id)
            counter = 0
            # busca en todos los reviews
            for rec_id in rec_ids:
                recipe = self.recipes.get_recipe(rec_id)
                # mira si coincide el id de la receta 'en' la review y de la id de la receta
                if recipe.get_id() == chef_id:
                    chef.add_score(recipe.get_score())
                    counter += 1

            chef_score = chef.get_score()
            # hace la media del score
            try:
                chef.set_score(chef_score/counter)
            except ZeroDivisionError:
                continue

    def normalize_chefs_scores(self):
        # Complete this function
        max_score = self.chefs.get_top_n(-1)[0].get_score()
        min_score = self.chefs.get_top_n(1)[0].get_score()
        id_list = self.chefs.get_ids()
        for id in id_list:
            chef = self.chefs.get_chef(id)
            raw_score = chef.get_chef()
            norm_score = (raw_score-min_score)/(max_score-min_score)
            chef.score = norm_score

    def sort_structures(self):
        self.chefs.sort_chefs()
        self.recipes.sort_recipes()
        self.reviews.sort_reviews()

    def get_top_n_chefs(self, n=1):
        # Complete this function
        top_chefs = self.chefs.get_top_n(n)
        return top_chefs

    def get_top_n_recipes(self, n=1):
        # Complete this function
        top_recipes = self.recipes.get_top_n(n)
        return top_recipes

    def get_top_n_reviews(self, n=1):
        # Complete this function
        top_reviews = self.reviews.get_top_n(n)
        return top_reviews

    def show_chefs(self, chefs):
        # Complete this function
        if 0 > chefs > len(self.chefs):
            for chef in chefs:
                print()
                print(str(chef))
        else:
            raise TopChefException("Chefs index out of range")

    def show_recipes(self, recipes):
        # Complete this function
        if 0 > recipes > len(self.recipes):
            for recipe in recipes:
                print()
                print(str(recipe))
        else:
            raise TopChefException("Recipe index out of range")

    def show_reviews(self, reviews):
        # Complete this function
        if 0 > reviews > len(self.reviews):
            for review in reviews:
                print()
                print(str(review))
        else:
            raise TopChefException("Reviews index out of range")

