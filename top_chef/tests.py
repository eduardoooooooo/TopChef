from TopChef.top_chef.controllers.TopChef import TopChef
from TopChef.top_chef.controllers.word_dictionary import WordDictionary

if __name__ == '__main__':
    topchef = TopChef()
    topchef.load_data("../data/topchef_data.txt")
    word_dictionary = WordDictionary()
    word_dictionary.load_words("../data/words.txt")
    topchef.compute_reviews_score(word_dictionary)
    print("Sorted")
    topchef.sort_structures()
    a=topchef.reviews.sorted_reviews
    for i in range(len(a)):
        print(a[i])
    topchef.compute_recipes_score()


