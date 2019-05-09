# Structure to hold the reviews
from TopChef.top_chef.controllers.InsertionSort import InsertionSort
from TopChef.top_chef.models.Review import Review


class Reviews:
    def __init__(self):
        self.reviews = {}
        self.next_review = 0
        self.sorted_reviews = []

    def add_review(self, rec_id, review):
        self.next_review += 1
        new_review = Review(self.next_review, review, rec_id)
        self.reviews[new_review.get_id()] = new_review
        self.sorted_reviews.append(new_review)

        return new_review

    def get_ids(self):
        # Complete this function
        return list(self.reviews.keys())

    def exists(self, id):
        # Complete this function
        return False

    def get_review(self,rev_id):
        # Complete this function
        return self.reviews[rev_id]

    def min_score(self):
        # Complete this function
        return None

    def max_score(self):
        # Complete this function
        return None

    def is_sorted(self):
        """
        Comprueba que el array está ordenado.
        :return: True si esta ordenado y Falso en caso contrario.

        if len(self.sorted_reviews)>1:
            for i in range(len(self.sorted_reviews)-1):
                if self.sorted_reviews[i].get_score()> self.sorted_reviews[i+1].get_score():
                    return False
                if self.sorted_reviews[i].get_score() == self.sorted_reviews[i + 1].get_score():
                    if self.sorted_reviews[i].get_id() > self.sorted_reviews[i + 1].get_id():
                        return False
            return True
        return True
        """
        return False

    def sort_reviews(self):
        """
        Ordena el array self.sorted_reviews
        :return:
        """
        if self.is_sorted():
            return
        else:
            insertion_sort = InsertionSort(self.sorted_recipes)
            insertion_sort.sort()

    def get_top_n(self, n=1):
        # Complete this function
        return None

    def __str__(self):
        # Complete this function
        rev_str = ""
        return rev_str
