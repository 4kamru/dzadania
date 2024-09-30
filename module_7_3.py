# Задача "Найдёт везде"
class WordsFinder:
    def __init__(self, *args):
        self.file_names  = args

    # получение списка файлов и вывод результатов чтения всех слов
    def get_all_words(self):
        res = {}
        for name in self.file_names:
            one_word = self._get_f_words(name)
            res[name] = one_word
        return res  # возможно, придется приводить к типу dict

    # внутренний метод для чтения и поиска в файле + замены запрещенных символов
    def _get_f_words(self,file_name):
        # запрещённые символы
        rest_symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        res = ''
        # открываем файл, читаем, приводим текст к нижнему регистру
        with open(file_name, 'r', encoding='utf-8') as file:
            txt = file.read().lower()
            # ищем и заменяем запрещенные символы пробелами
            for one_symbol in rest_symbols:
                txt = txt.replace(one_symbol,' ')
                res = txt.split()

            return res

    def find(self, word):
        res = {}
        for file_name, words in self.get_all_words().items():
            if word.lower() in words:
                pos = words.index(word.lower()) + 1
                res[file_name] = pos

        return res

    def count(self, word):
        res = {}
        for name, words in self.get_all_words().items():
            count = words.count(word.lower())
            if count > 0:
                res[name] = count

        return res


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего


finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
print(finder1.get_all_words())
print(finder1.find('Child'))
print(finder1.count('Child'))

finder1 = WordsFinder('Rudyard Kipling - If.txt',)

print(finder1.get_all_words())
print(finder1.find('if'))
print(finder1.count('if'))

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')

print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))


