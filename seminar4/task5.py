# Сделана после сдачи ДЗ

from task4 import createEquation

def readEquation():
    firstEquation = createEquation()
    equation = {}

    firstEquation = firstEquation.replace(" + ", " +").replace(" - ", " -").split()[:-2]

    for i in range(len(firstEquation)):
            firstEquation[i] = firstEquation[i].replace("+", "").split("x^")     # split разделяем по знаку - x^
            equation[int(firstEquation[i][1])] = int(firstEquation[i][0])  # [i] - ключ (здесь ключ - это степень), [1] - коэф-нт = меняем местами
    
    return equation   # возвращает словарь

finalWord = {}
word1 = readEquation()
word2 = readEquation()

for i in range(max(len(word1), len(word2)), -1, -1):
    first = word1.get(i)
    second = word2.get(i)
    if first != None or second != None:
        finalWord[i] = (first if first != None else 0) + (second if second != None else 0)

print(finalWord)

print(word1)
print(word2)

