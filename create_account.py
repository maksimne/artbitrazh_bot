import random
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


from config import email, password

useragents = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/130.0.2849.80",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/130.0.2849.80",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/114.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/114.0.0.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/114.0.0.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 OPR/114.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Vivaldi/7.0.3495.14",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Vivaldi/7.0.3495.14",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_7_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Vivaldi/7.0.3495.14",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Vivaldi/7.0.3495.14",
    "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Vivaldi/7.0.3495.14",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 YaBrowser/24.10.1.669 Yowser/2.5 Safari/537.36",
]


def get_useragent():
    return useragents[random.randint(0, len(useragents)-1)]



def register_device():
    username = "".join([random.choice("abcdefghijklmn1234567890") for i in range(16)])
    password = "".join([random.choice("abcdefghijklmn1234567890-!@#$%QWERTYUIOPASDFGHJKLZXCVBNM") for i in range(16)])

    return [username, password]


def tiktok_auth(url, email, username, password):

    options = webdriver.ChromeOptions()
    useragent = get_useragent()

    print(useragent)

    options.add_argument(f"user-agent={useragent}")
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)

    try:

        # переход на url
        driver.get(url=url)

        cookies = driver.get_cookies()
        cookies = cookies[len(cookies)-1]

        driver.delete_all_cookies()

        driver.add_cookie(cookies)

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
    username, password = register_device()
    tiktok_auth("https://www.tiktok.com/signup", "formak026@gmail.com", username, password)


if __name__ == "__main__":
    main()