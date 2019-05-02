from TopChef.top_chef.controllers.TopChef import TopChef
from TopChef.top_chef.controllers.word_dictionary import WordDictionary

if __name__ == '__main__':
    topchef = TopChef()
    topchef.load_data("../data/topchef_data.txt")
    word_dictionary = WordDictionary()
    word_dictionary.load_words("../data/words.txt")
