animals = ['Кошка', 'Собака', 'Слон', 'Жираф', 'Змея', 'Крокодил']
# Если не указать старт, то по умолчанию начнём с 0. Указываем две переменные между for и in.
# В переменную i (счётчик) мы помещаем число (с единицы). А в переменную animal помещаем животное.
# Цикл заканчивается, когда все элементы в списке выведены.
# Ф-ия enumerate позволяет нумеровать элементы
for i, animal in enumerate(animals, start=1):
    print(i, animal)