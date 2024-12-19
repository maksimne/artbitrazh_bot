import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from config import email, password


def tiktok_auth(url, email):

    driver = webdriver.Chrome()

    try:

        # переход на url
        driver.get(url=url)
        driver.delete_all_cookies()

        # ожидание загрузки страницы ВАЖНО!!!!!!!!!!
        time.sleep(5)

        # регистрация в тик ток
        driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div/div[1]/div/div[2]/div[2]').click()
        driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[4]/a').click()

        email_field = driver.find_element(By.NAME, 'email')
        # ввод email ВАЖНO
        time.sleep(random.randint(50, 100)/100)
        email_field.send_keys(email)
        time.sleep(random.randint(100, 200)/100)

        password_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[6]/div/input')
        time.sleep(random.randint(50, 100)/100)

        # вводим пароль ВАЖНО
        password = "hjdfbjkasdh7457234"
        password_field.send_keys(password)


        # Указываем дату рождения
        day_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[2]')
        day_field.click()
        time.sleep(random.randint(50, 100) / 100)

        for i in range(random.randint(1,28)):
            day_field.send_keys(Keys.ARROW_DOWN)  # Случайный day
            time.sleep(random.randint(10, 20) / 100)

        day_field.send_keys(Keys.RETURN)
        time.sleep(random.randint(100, 400) / 100)

        year_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[3]')
        year_field.click()
        time.sleep(random.randint(50, 100) / 100)

        for i in range(random.randint(18, 34)):
            year_field.send_keys(Keys.ARROW_DOWN)  # Случайный year
            time.sleep(random.randint(10, 20) / 100)

        year_field.send_keys(Keys.RETURN)
        time.sleep(random.randint(100, 400) / 100)

        month_field = driver.find_element(By.XPATH, '//*[@id="loginContainer"]/div[1]/form/div[2]/div[1]')
        month_field.click()
        time.sleep(random.randint(50, 100) / 100)

        for i in range(random.randint(0, 11)):
            month_field.send_keys(Keys.ARROW_DOWN)  # Случайный month
            time.sleep(random.randint(10, 20) / 100)

        month_field.send_keys(Keys.RETURN)
        time.sleep(random.randint(100, 400) / 100)

        # send code
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div[1]/form/div[7]/div/button').click()

        time.sleep(random.randint(200, 500) / 100)
        time.sleep(100)
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


def main():
    tiktok_auth("https://www.tiktok.com/signup", "formak026@gmail.com")


if __name__ == "__main__":
    main()