# 1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = []
nums = input('Введите список чисел через пробел: \n').split()
for i in nums:
    my_list.append(int(i))

new_list = []
for elem in set(my_list):
    if my_list.count(elem) > 1:
        new_list.append(elem)

print(f'Исходный список -->> {my_list}\nРезультирующий список -->> {new_list}')