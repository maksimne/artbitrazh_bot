import requests
import time

BASE_URL = "https://api.mail.tm"

ctime = int(time.time());


def create_email():
    """Создает временный почтовый адрес."""
    # Получение доступных доменов
    domains = requests.get(f"{BASE_URL}/domains").json()
    print(domains['hydra:member'][0]['domain'])
    domain = domains['hydra:member'][0]['domain']  # Выбираем первый доступный домен

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
    return data['id'], data['address'], password


def get_token(email, password):
    """Получает токен для авторизации."""
    response = requests.post(f"{BASE_URL}/token", json={
        "address": email,  # Используем email, который был получен при регистрации
        "password": password
    })

    # Отладка: выводим полный ответ сервера, чтобы понять причину ошибки
    if response.status_code != 200:
        print(f"Ошибка при получении токена: {response.status_code}")
        print(f"Ответ от сервера: {response.text}")
        response.raise_for_status()  # Это вызовет ошибку, если код не 200

    return response.json()['token']

def get_messages(token):
    """Получает список писем."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/messages", headers=headers)
    response.raise_for_status()
    return response.json()

def read_message(token, message_id):
    """Читает содержимое письма."""
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/messages/{message_id}", headers=headers)
    response.raise_for_status()
    return response.json()

if __name__ == "__main__":
    # Создание временного почтового ящика
    account_id, email, password = create_email()
    print(f"Создан почтовый адрес: {email}")

    # Получение токена авторизации
    token = get_token(email, password)
    print(f"Токен авторизации получен: {token}")

    # Проверка новых писем
    print("Ожидание новых писем...")
    while True:
        messages = get_messages(token)
        if messages['hydra:totalItems'] > 0:
            print(f"Найдено {messages['hydra:totalItems']} письмо(а).")
            for message in messages['hydra:member']:
                msg = read_message(token, message['id'])
                print(f"От: {msg['from']['address']}")
                print(f"Тема: {msg['subject']}")
                print(f"Содержимое: {msg['intro']}")
            break
        time.sleep(5)
