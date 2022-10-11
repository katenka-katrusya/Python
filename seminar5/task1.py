# Напишите программу, удаляющую из текста все слова, содержащие "абв"

string = "dsms 12mgk 3 11; p srvkmm cbdd, ;ps03l[- -- vnd"
print(f"\nДана строка: {string}")

element = input("Введите элемент, который хотите удалить: ")

if element not in string:
    print(f"Данного элемента нет в строке")
else: 
    result = string.replace(element, '')
    print(f"Новая строка: {result}\n")
