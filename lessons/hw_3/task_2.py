# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import string

SHOW_WORDS = 10

with open('text.txt', encoding='utf-8') as f:
    text = f.read()

words = text.translate(str.maketrans('', '', string.punctuation)).lower().split()
# print(res)

word_count = dict()
for word in words:
    if len(word) > 0:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1

for i, word in enumerate(sorted(word_count, key=word_count.get, reverse=True)[:SHOW_WORDS]):
    print(f'{i + 1} Слово "{word}" встречается {word_count[word]} раз')
