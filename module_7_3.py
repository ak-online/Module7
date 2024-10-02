import string
import os.path


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        global all_words
        self.all_words = {}
        for openname in self.file_names:
            if os.path.exists(openname):
                with open(openname, 'r', encoding='utf-8') as file:
                    fulltxt = file.read().lower()
                    for punct in string.punctuation:
                        fulltxt = fulltxt.replace(punct, "")
                    self.all_words[openname] = fulltxt.split()
            else:
                print(f'Файл - {openname} не существует.')
                # self.all_words = False
        return self.all_words

    def find(self, word):
        word_index = {}
        word = word.lower()
        for f_name, words in self.all_words.items():
            word_index[f_name] = words.index(word) + 1
        return word_index

    def count(self, word):
        word_count = {}
        word = word.lower()
        for f_name, words in self.all_words.items():
            word_count[f_name] = words.count(word)
        return word_count

# ----------------------------------------------

finder2 = WordsFinder('test.txt')
print(finder2.get_all_words())  #  Все слова если есть файл
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

finder3 = WordsFinder('products.txt')
print(finder3.get_all_words())  # Все слова если есть файл
print(finder3.find('34'))  # 5 слово по счёту
print(finder3.count('teXT'))  # 0 слова teXT в тексте всего

finder1 = WordsFinder('1test.txt')
print(finder1.get_all_words())  # Все слова если есть файл
