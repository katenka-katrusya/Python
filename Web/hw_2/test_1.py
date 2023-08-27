import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
site = Site(testdata["address"])


def test_step1():
    x_selector1 = """//*[@id="login"]/div[1]/label/input"""
    input1 = site.find_element("xpath", x_selector1)
    input1.send_keys("test")
    x_selector2 = """//*[@id="login"]/div[2]/label/input"""
    input2 = site.find_element("xpath", x_selector2)
    input2.send_keys("test")
    btn_selector = "button"
    btn = site.find_element("css", btn_selector)
    btn.click()
    x_selector3 = """//*[@id="app"]/main/div/div/div[2]/h2"""
    err_label = site.find_element("xpath", x_selector3)
    assert err_label.text == "401"


def add_post():
    # Ввод названия поста
    post_title = "New post"
    post_title_selector = '//*[@id="update-post-item"]/div/div/div[1]/div/label/input'
    input_post_title = site.find_element("xpath", post_title_selector)
    input_post_title.send_keys(post_title)

    # Ожидание перед нажатием кнопки создания поста
    time.sleep(1)  # Задержка в секундах

    # Нажатие кнопки создания поста
    create_post_button_selector = '//*[@id="create-btn"]'
    create_post_button = site.find_element("xpath", create_post_button_selector)
    create_post_button.click()

    # Ожидание после нажатия кнопки создания поста
    time.sleep(1)  # Задержка в секундах

    # Проверка наличия названия поста на странице
    post_title_selector = '//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'
    post_title_element = site.find_element("xpath", post_title_selector)
    assert post_title_element.text == post_title
