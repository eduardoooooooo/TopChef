import re
class FormatWordScore:
    def __init__(self,string):
        self.string = string
    def format_string_score(self):
        string_lower = self.string.lower()
        string_lower_only_letters = re.sub('[^a-zA-Z\s+]+', '', string_lower)  # borra todo lo que no es una letra
        review_lower_only_letters_array=string_lower_only_letters .split()
        return review_lower_only_letters_array