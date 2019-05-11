import os

from TopChef.top_chef.Exceptions.WordDictionaryException import WordDictionaryException


class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
        # Complete this function
        if os.stat(word_path).st_size == 0:
            raise WordDictionaryException("Ningun dato ha sido cargado.El fichero: "+word_path + " está vacio.")
        word_dictionary = open(word_path,"r")
        word_dictionary.readline()
        line=word_dictionary.readline().replace("\n","").split("\t")
        while len(line)>1 :
            try:
                self.words[line[0]]=float(line[1])
                line = word_dictionary.readline().replace("\n","").split("\t")
            except ValueError:
                print("Fichero erroneo. El valor no se podido convertir a float")

    def clear(self):
        """
        Reinicia  los valores
        :return:
        """
        self.__init__()
    def add_word(self, word, value):
        self.words[word] = value

    def exists(self, word):
        return word in self.words

    def get_value(self, word):
        return self.words[word]

    def get_words(self):
        return self.words.keys()

    def __str__(self):
        word_str = ""
        for word in self.words:
            word_str += word + ": " + str(self.words[word]) + "\n"
        return word_str

    def __len__(self):
        return len(self.words)