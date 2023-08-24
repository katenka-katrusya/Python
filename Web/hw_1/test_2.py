import requests
import yaml


with open('config.yaml') as file:
    my_dict = yaml.safe_load(file)

url = my_dict['url']
url_1 = my_dict['url_1']
username = 'Captain'
password = 'bc9d8ff48a'


def login(username, password):
    obj_data = requests.post(url=url, data={'username': username, 'password': password})
    # print(obj_data.json())
    token = obj_data.json()['token']
    # print(token)
    return token

def token_auth(token):
    response = requests.get(url=url_1, headers={'X-Auth-Token': token}, params={'owner': 'notMe'})
    content_var = [item['content'] for item in response.json()['data']]
    return content_var

def test_step2(login):
    assert 'content' in token_auth(login)

def test_step3(login):
    # Создание нового поста
    new_post = {
        'title': 'New Post',
        'description': 'This is a new post',
        'content': 'Some content for the new post'
    }
    response = requests.post(url=url_1, headers={'X-Auth-Token': login}, json=new_post)

    # Проверка наличия созданного поста по полю "описание"
    response = requests.get(url=url_1, headers={'X-Auth-Token': login})

    posts = response.json()['data']
    assert any(post['description'] == 'This is a new post' for post in posts)

# if __name__ == '__main__':
#     print(token_auth(login(username, password)))