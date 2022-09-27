# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# если ввести числа 1, 2, 3 - утверждение будет истинно.

print("Введите координаты x, y, z")
x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))

a = x * y * z
b = x + y + z

if a > 0: 
    a = 0
elif a < 1:
    a = 1
if b > 0:
    b = 0
elif b < 1:
    b = 1
if a == b:
    print("Утверждение истинно")
elif a != b:
    print("Утверждение ложно")

# способ, правильный:
trigger = True # флаг

for x in [True, False]:          # range(2)
    for y in [True, False]:      # range(2)
        for z in [True, False]:  # range(2)
           if not (x or y or z) != (not x and not y and not z):
            print("Неверно")
            trigger = False
            break

if trigger: print("Выражение верно")
