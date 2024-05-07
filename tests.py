from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest

link = "http://localhost:5000/"
link_1="http://localhost:5000/login"
link_2="http://localhost:5000/signup"
class TestRegForm_home(unittest.TestCase):
# Проверяем открытие сайта, отображение и кликабельность вкладок и окон во вкладках
    def test_positive_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link)  
            time.sleep(3)

            home_page=browser.find_element(By.CSS_SELECTOR,'[href="/"]')
            home_page.click()
            time.sleep(2)
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Test home page')
            time.sleep(1)
            log_page=browser.find_element(By.CSS_SELECTOR,'[href="/login"]')
            log_page.click()
            time.sleep(1)
            input_u_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Email"]')
            assert input_u_email.is_displayed()
            time.sleep(1)
            input_u_email.click()
            input_u_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Password"]')
            assert input_u_password.is_displayed()
            time.sleep(1)
            input_u_password.click()
            checkbox= browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
            assert checkbox.is_displayed()
            time.sleep(1)
            checkbox.click()
            button_log = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            assert button_log.is_displayed()
            time.sleep(1)
            button_log.click()

            sing_up_page=browser.find_element(By.CSS_SELECTOR,'[href="/signup"]')
            assert sing_up_page.is_displayed
            time.sleep(1)
            sing_up_page.click()
            input_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Email"]')
            assert input_email.is_displayed()
            time.sleep(1)
            input_email.click()
            input_name=browser.find_element(By.CSS_SELECTOR,'[placeholder="Name"]')
            assert input_name.is_displayed()
            time.sleep(1)
            input_name.click()
            input_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Password"]')
            assert input_password.is_displayed()
            time.sleep(1)
            input_password.click()
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            assert button_singup.is_displayed()
            time.sleep(1)
            button_singup.click()
        finally:
            time.sleep(5)
            browser.quit()


# Заполняем корректно все поля,регистрируем пользователя, заходим под учетной записью пользователя, выходим из учетной записи
    def test_positive_2(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_2)  
            time.sleep(3)
            input_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Email"]')
            input_email.send_keys('alisavoloshina@mail.ru')
            time.sleep(1)
            input_name=browser.find_element(By.CSS_SELECTOR,'[placeholder="Name"]')
            input_name.send_keys('Alisa')
            time.sleep(1)
            input_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Password"]')
            input_password.send_keys('alisagav')
            time.sleep(1)
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Login')

            input_u_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Email"]')
            input_u_email.send_keys("alisavoloshina@mail.ru")
            time.sleep(1)
            input_u_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Password"]')
            input_u_password.send_keys('alisagav')
            time.sleep(1)
            checkbox= browser.find_element(By.CSS_SELECTOR,'[type="checkbox"]')
            checkbox.click()
            button_log = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            time.sleep(1)
            button_log.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Welcome, Alisa!')

            log_out_page=browser.find_element(By.CSS_SELECTOR,'[href="/logout"]')
            assert log_out_page.is_displayed
            time.sleep(1)
            log_out_page.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Test home page')

        finally:
            time.sleep(3)
            browser.quit()


# Заполняем корректно все поля,кроме необязательных регистрируем пользователя,заходим под учетной записью пользователя,выходим из учетной записи
    def test_positive_3(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_2)  
            time.sleep(3)
            input_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Email"]')
            input_email.send_keys('alisavoloshin@mail.ru')
            time.sleep(1)
            input_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Password"]')
            input_password.send_keys('alisagav')
            time.sleep(1)
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Login')

            input_u_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Email"]')
            input_u_email.send_keys("alisavoloshin@mail.ru")
            time.sleep(1)
            input_u_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Password"]')
            input_u_password.send_keys('alisagav')
            time.sleep(1)
            button_log = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            time.sleep(1)
            button_log.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Welcome, !')
            time.sleep(1)
            log_out_page=browser.find_element(By.CSS_SELECTOR,'[href="/logout"]')
            assert log_out_page.is_displayed
            time.sleep(1)
            log_out_page.click()
            aria_hidden=browser.find_element(By.CLASS_NAME,'title').text
            self.assertEqual(aria_hidden,'Test home page')

        finally:
            time.sleep(3)
            browser.quit()


# Проверка полей на странице Sign Up. Все поля незаполненные.
    def test_negative_1(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_2)  
            time.sleep(2)

            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            aria_hidden=browser.find_element(By.CSS_SELECTOR,"[class='notification is-danger']").text
            self.assertEqual(aria_hidden,'Email address already exists. Go to login page.')

# Заполнено только поле емайл
            input_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Email"]')
            input_email.send_keys('alisa_0@mail.ru')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()

        finally:
            time.sleep(3)
            browser.quit()


# Проверка поля Email на странице Sign Up
    def test_negative_email_signup(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_2)  
            time.sleep(2)

            input_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Email"]')
            input_email.send_keys('1')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(1)
            input_email.clear()
            input_email.send_keys('a')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(1)
            input_email.clear()
            input_email.send_keys('#')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(1)
            input_email.clear()
            input_email.send_keys('@')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(1)
            input_email.clear()
            input_email.send_keys('алиса@mail.ru')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(1)
            input_email.clear()
            input_email.send_keys('alisa@mail@ru.ru')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(2)
            input_email.clear()
            input_email.send_keys('*&^%$#*><@pop.tut')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(2)
            input_email.clear()
            input_email.send_keys('AliСА@mailru')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(2)
            input_email.clear()
            input_email.send_keys('alisamail.ru')
            button_singup = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            button_singup.click()
            time.sleep(2)
            input_email.clear()

        finally:
            time.sleep(3)
            browser.quit()


# Проверка полей на странице Login. Все поля незаполненные.
    def test_negative_(self):
        try:
            browser = webdriver.Chrome()
            browser.get(link_1)  
            time.sleep(2)

            button_log = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            time.sleep(1)
            button_log.click()
            aria_hidden=browser.find_element(By.CSS_SELECTOR,"[class='notification is-danger']").text
            self.assertEqual(aria_hidden,'Please check your login details and try again.')

# Поля заполнены некорректно(незарегистрированый пользователь)
            input_u_email=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Email"]')
            input_u_email.send_keys("noname@mail.ru")
            time.sleep(1)
            input_u_password=browser.find_element(By.CSS_SELECTOR,'[placeholder="Your Password"]')
            input_u_password.send_keys('123')
            time.sleep(1)
            button_log = browser.find_element(By.CSS_SELECTOR,'[class="button is-block is-info is-large is-fullwidth"]')
            time.sleep(1)
            button_log.click()
            aria_hidden=browser.find_element(By.CSS_SELECTOR,"[class='notification is-danger']").text
            self.assertEqual(aria_hidden,'Please check your login details and try again.')

        finally:
            time.sleep(3)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
