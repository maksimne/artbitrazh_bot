from faker import Faker
import requests


def generate_profile():
    fake = Faker()
    name = fake.first_name() + fake.last_name()
    bio = fake.sentence(nb_words=10)

    avatar_url = "https://thispersondoesnotexist.com/image"
    avatar_path = "avatar.jpg"
    response = requests.get(avatar_url)
    with open(avatar_path, "wb") as f:
        f.write(response.content)

    return {
        "name": name,
        "bio": bio,
        "avatar": avatar_path
    }

print(generate_profile())