import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# from config import email, password


def tiktok_auth(url):
    driver = webdriver.Chrome()

    try:
        # переход на url
        driver.get(url=url)
        # ожидание загрузки страницы ВАЖНО!!!!!!!!!!
        time.sleep(5)

        # регистрация в тик ток
        driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[4]/a').click()

        email_field = driver.find_element(By.NAME, 'email')
        # ввод email ВАЖНО
        email = "godonukm@gmail.com"
        email_field.send_keys(email)

        password_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[6]/div/input')
        # вводим пароль ВАЖНО
        password = "abdulbek_bot111"
        password_field.send_keys(password)

        # Указываем дату рождения
        day_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]')
        day_field.click()
        day_field.send_keys(Keys.ARROW_DOWN * random.randint(1, 28))  # Случайный день
        day_field.send_keys(Keys.RETURN)

        year_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]')
        year_field.click()
        year_field.send_keys(Keys.ARROW_DOWN * random.randint(1999, 2005))  # Случайный день
        year_field.send_keys(Keys.RETURN)

        month_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]')
        month_field.click()
        driver.find_element(By.XPATH, '//*[@id="Month-options-item-2"]').click()

        # send code
        driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[6]/div/div').click()
        time.sleep(5)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    tiktok_auth("https://www.tiktok.com/signup")


if __name__ == "__main__":
    main()