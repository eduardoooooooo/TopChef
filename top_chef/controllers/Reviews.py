# Structure to hold the reviews
from TopChef.top_chef.models.Review import Review


class Reviews:
    def __init__(self):
        self.reviews = {}
        self.next_review = 0
        self.sorted_reviews = []

    def add_review(self, rec_id, review):

        new_review = Review(self.next_review, review, rec_id)
        self.reviews[new_review.get_id] = new_review
        self.next_review += 1
        return new_review

    def get_ids(self):
        # Complete this function
        return list(self.reviews.keys())

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
