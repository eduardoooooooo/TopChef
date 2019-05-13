class WordDictionaryException(Exception):
    pass

class WordDictionary:

    def __init__(self):
        self.words = {}

    def load_words(self, word_path):
        """
        Lee la primera linea para ver si es el fichero deseado, sino raise WordDictionaryException.
        Después lee las demás lineas y llama a la función add_word()

        :param word_path: (Objeto)  Fichero que se desea realizar la operación
        """
        # Complete this function
        WORD = "WORD"
        VALUE = "VALUE"

        self.clean()
        
        # con el with no es necesario cerrar el fichero ya que si sale de éste se cierra directamente
        with open(word_path,'r') as f:
            line = f.readline()
        
            if (WORD and VALUE) not in line:
                raise WordDictionaryException('Wrong path')

            for line in f:

                if line == "\n":
                    raise WordDictionaryException("Empty line in the path")

                try:
                    lista = line.split()
                    word, value = lista
                    self.add_word(word, float(value))
                    
                except ValueError:
                    raise WordDictionaryException("Error path format")

    def clean(self):
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