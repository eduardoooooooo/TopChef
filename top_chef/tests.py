from TopChef.top_chef.controllers.TopChef import TopChef
from TopChef.top_chef.controllers.word_dictionary import WordDictionary

if __name__ == '__main__':

    topchef = TopChef()
    topchef.load_data("../data/topchef_data_alt.txt")
    word_dictionary = WordDictionary()
    word_dictionary.load_words("../data/words_alt.txt")
    topchef.compute_reviews_score(word_dictionary)
    topchef.compute_recipes_score()
    topchef.compute_chefs_score()
    topchef.sort_structures()
    """
    print("-------------SORTED REVIEWS--------------")
    a = topchef.reviews.sorted_reviews
    for i in range(len(a)):
        print(a[i])

    print("-------------SORTED RECIPES--------------")
    a = topchef.recipes.sorted_recipes
    for i in range(len(a)):
        print(a[i])

    print("-------------SORTED CHEFS----------------")
    a = topchef.chefs.sorted_chefs
    for i in range(len(a)):
        print(a[i])

    topchef.show_chefs(topchef.chefs.sorted_chefs)
    topchef.show_recipes(topchef.recipes.sorted_recipes)
    """
    #topchef.show_chefs(topchef.chefs.sorted_chefs)
    a="aaaa\naaaaa"
    print(a)
    print(a.split())