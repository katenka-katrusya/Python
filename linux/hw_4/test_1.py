from sshcheckers import ssh_checkout, upload_files
import yaml


class SSHTest:
    def __init__(self):
        with open('config.yaml') as f:
            self.data = yaml.safe_load(f)

    def test_positive(self):
        res = []

        # Подключение по SSH
        res.append(ssh_checkout(self.data.get("ip"), self.data.get("user"), self.data.get("passwd"), "echo Connected to SSH"))

        # Загрузка файлов по SSH
        res.append(upload_files(self.data.get("ip"), self.data.get("user"), self.data.get("passwd"),
                                self.data.get("local_path"), self.data.get("remote_path")))

        # Выполнение команды по SSH и проверка результатов
        res.append(ssh_checkout(self.data.get("ip"), self.data.get("user"), self.data.get("passwd"),
                                f"echo {self.data.get('passwd')} | sudo -S dpkg -i {self.data.get('remote_path')}", "Настраивается пакет"))
        res.append(ssh_checkout(self.data.get("ip"), self.data.get(""), self.data.get("passwd"),
                                f"echo {self.data.get('passwd')} | sudo -S dpkg -s p7zip-full", "Status: install ok installed"))

        return all(res)

    def test_negative(self):
        res = []

        # Подключение по SSH
        res.append(ssh_checkout(self.data.get("invalid_ip"), self.data.get("user"), self.data.get("passwd"), "echo Connected to SSH"))

        # Загрузка файлов по SSH
        res.append(upload_files(self.data.get("ip"), self.data.get("user"), self.data.get("passwd"),
                                "non_existent_file.txt", self.data.get("remote_path")))

        # Выполнение команды по SSH и проверка результатов
        res.append(ssh_checkout(self.data.get("ip"), self.data.get("user"), self.data.get("passwd"),
                                "invalid_command", "Expected output"))

        return all(res)


test_obj = SSHTest()
print(test_obj.test_positive())
print(test_obj.test_negative())
