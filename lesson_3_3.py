import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestUniquenessSelectors(unittest.TestCase):
    def test_for_registration_1(self):
        # Инициализация подключения
        url = 'http://suninjuly.github.io/registration1.html'
        driver = webdriver.Edge()
        driver.get(url)
        driver.implicitly_wait(5)

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
        welcome_text = driver.find_element(by=By.TAG_NAME, value='h1').text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Failed registration')

        # Проверяем визуально отображение приветствия и закрываем соединение
        driver.quit()

    def test_for_registration_2(self):
        # Инициализация подключения
        url = 'http://suninjuly.github.io/registration2.html'
        driver = webdriver.Edge()
        driver.get(url)
        driver.implicitly_wait(5)

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
        welcome_text = driver.find_element(by=By.TAG_NAME, value='h1').text
        self.assertEqual('Congratulations! You have successfully registered!', welcome_text, 'Failed registration')

        # Проверяем визуально отображение приветствия и закрываем соединение
        driver.quit()


if __name__ == "__main__":
    unittest.main()
