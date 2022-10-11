# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

pathRead = r'PythonSeminars\seminar5\data.txt'
pathWrite = r'PythonSeminars\seminar5\data2.txt'

def encoding(message): 
    encode = ''

    i = 0
    while i < len(message):
        count = 1
        while i + 1 < len(message) and message[i] == message[i + 1]:
            count += 1
            i += 1
        encode += str(count) + message[i]
        i += 1
    
    return encode

def decoding(message): 
    decode = ''
    count = ''

    for elem in message:
        if elem.isdigit():
            count += elem
        else:
            decode += elem * int(count)
            count = ''
    return decode

try:
    with open(pathRead, 'r') as data:
        str1 = data.readline()
        # print(str1, end='')
        str2 = data.readline()
        # print(str2)
except:
    print("Файл не найден")

try:
    with open(pathWrite, 'w') as data:
        data.write(encoding(str1))
        data.write(decoding(str2))       
except:
    print("Файл не найден")

# ЕСТЬ ПРОБЛЕМА! При выводе данных в отдельный файл при кодировании, результат записывается правильно, но в конце добавляется цифра 1.
# А если результат выводить в терминал, то никакой лишней цифры в конце нет, всё выводится правильно. Я проблему не смогла решить