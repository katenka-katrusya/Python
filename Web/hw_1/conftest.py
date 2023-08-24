import pytest
import requests
import yaml

with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url_1 = my_dict['url_1']
username = 'Captain'
password = 'bc9d8ff48a'

@pytest.fixture()
def login(username='Captain', password='bc9d8ff48a'):
    obj_data = requests.post(url=url, data={'username': username, 'password': password})
    # print(obj_data.json())
    token = obj_data.json()['token']
    # print(token)
    return token