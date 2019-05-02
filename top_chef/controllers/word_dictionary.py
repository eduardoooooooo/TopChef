class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
        # Complete this function
        word_dictionary = open(word_path,"r")
        word_dictionary.readline()
        line=word_dictionary.readline().replace("\n","").split("\t")
        while len(line)>1 :
            self.words[line[0]]=line[1]
            line = word_dictionary.readline().replace("\n","").split("\t")


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