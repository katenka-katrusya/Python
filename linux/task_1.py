import subprocess

def check_output(command, text):
    try:
        output = subprocess.check_output(command, shell=True, encoding='utf-8')
        if text in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False

command = "ls -l"
text = "file.txt"

result = check_output(command, text)
print(result)
