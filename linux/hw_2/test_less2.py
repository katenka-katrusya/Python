import subprocess
import os


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


falderin = '/home/user/tst'
falderout = '/home/user/out'
# print(checkout('cd /home/user/tst; 7z a /home/user/arh1', 'Everything is Ok'))


def test_step1():
    assert checkout(f'cd {falderin}; 7z a {falderout}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {falderin}; 7z u {falderout}/arh1', 'Everything is OK'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {falderin}; 7z d {falderout}/arh1', 'Everything is Ok'), 'test3 FAIL'


def test_step4():
    # Проверка команды вывода списка файлов
    assert checkout(f'cd {falderin}; 7z l {falderout}/arh1', 'Everything is Ok'), 'test4 FAIL'


def test_step5():
    # Проверка команды разархивирования с путем к файлу
    assert checkout(f'cd {falderin}; 7z x {falderout}/arh1 -o{falderout}', 'Everything is Ok'), 'test5 FAIL'


def calculate_crc32():
    file_path = '/home/user/myfile.txt'
    cmd = f'crc32 {file_path}'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    return result.stdout.strip()


def test_step6():
    # Рассчет и проверка хеша
    archive_path = f"{falderout}/arh1"
    desired_hash = calculate_crc32()
    assert checkout(f'cd {falderin}; 7z h {archive_path}', desired_hash), 'test6 FAIL'