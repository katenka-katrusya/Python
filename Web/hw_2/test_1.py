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

    time.sleep(1)

    # Нажатие кнопки создания поста
    create_post_button_selector = '//*[@id="create-btn"]'
    create_post_button = site.find_element("xpath", create_post_button_selector)
    create_post_button.click()

    time.sleep(1)

    # Проверка наличия названия поста на странице
    post_title_selector = '//*[@id="app"]/main/div/div[3]/div[1]/a[1]/h2'
    post_title_element = site.find_element("xpath", post_title_selector)
    assert post_title_element.text == post_title


def test_step2():
    # Кликнуть по кнопке "Contact"
    contact_us_button_selector = '//*[@id="app"]/main/nav/ul/li[2]/a'
    contact_us_button = site.find_element("xpath", contact_us_button_selector)
    contact_us_button.click()

    time.sleep(1)

    # Ввод данных в поля формы
    name_selector = '//*[@id="contact"]/div[1]/label/input'
    name_input = site.find_element("xpath", name_selector)
    name_input.send_keys("Test Name")

    email_selector = '//*[@id="contact"]/div[2]/label/input'
    email_input = site.find_element("xpath", email_selector)
    email_input.send_keys("test@example.com")

    message_selector = '//*[@id="contact"]/div[3]/label/span/textarea'
    message_input = site.find_element("xpath", message_selector)
    message_input.send_keys("Test message")

    # Кликнуть по кнопке
    submit_button_selector = '//*[@id="contact"]/div[4]/button/div'
    submit_button = site.find_element("xpath", submit_button_selector)
    submit_button.click()

    time.sleep(1)

    # Переключиться на alert
    alert = site.driver.switch_to.alert
    assert alert.text == "Form successfully submitted"
    alert.accept()
