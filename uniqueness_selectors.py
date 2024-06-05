import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Инициируем работу драйвера
url = 'http://suninjuly.github.io/registration1.html'
driver = webdriver.Edge()
driver.get(url)
time.sleep(1)

try:
    # Заполнение обязательных форм
    first_name_input = driver.find_element(by=By.XPATH, value='//div[@class="first_block"]'
                                                              '/div[@class="form-group first_class"]/input')
    first_name_input.send_keys('Ivan')

    last_name_input = driver.find_element(by=By.XPATH, value='//div[@class="first_block"]'
                                                             '/div[@class="form-group second_class"]/input')
    last_name_input.send_keys('Ivanov')

    email_input = driver.find_element(by=By.XPATH, value='//div[@class="first_block"]'
                                                         '/div[@class="form-group third_class"]/input')
    email_input.send_keys('iivanov@mail.ru')

    driver.find_element(by=By.TAG_NAME, value='button').click()

    # Проверяем прохождение регистрации
    time.sleep(1)
    welcome_text = driver.find_element(by=By.TAG_NAME, value='h1').text
    assert 'Congratulations! You have successfully registered!' == welcome_text
finally:
    # Проверяем визуально отображение приветствия и закрываем соединение
    time.sleep(5)
    driver.quit()
