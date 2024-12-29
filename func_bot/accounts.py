from database import add_account, get_account_by_mail, delete_account, get_account_by_author
import requests
import time


BASE_URL = "https://api.mail.tm"

ctime = int(time.time())


def creating_account(author: str, platform: int):
    domains = requests.get(f"{BASE_URL}/domains").json()
    print(domains['hydra:member'][0]['domain'])
    domain = domains['hydra:member'][0]['domain']

    email_address = f"example{ctime}@{domain}"
    password = "strong_password123"

    response = requests.post(f"{BASE_URL}/accounts", json={
        "address": email_address,
        "password": password
    })

    if response.status_code != 201:  # Код успешного создания
        print(f"Ошибка при создании аккаунта: {response.text}")
        response.raise_for_status()

    data = response.json()
    add_account(data['address'], password, platform=platform, author=author)
    return data['id'], data['address'], password


def chek_account():
    pass


def del_account():
    pass


def business_account():
    pass