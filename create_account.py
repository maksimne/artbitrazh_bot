from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--headless")  # Без графического интерфейса
driver = webdriver.Chrome(options=options)

driver.get("https://www.tiktok.com/signup")

# Заполнение формы регистрации
username_field = driver.find_element(By.NAME, "username")
username_field.send_keys("testsd")

email_field = driver.find_element(By.NAME, "email")
email_field.send_keys("sdfsdfsdf@mail.com")

password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("13234555sFF__ds")

# Отправка формы
submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
submit_button.click()
