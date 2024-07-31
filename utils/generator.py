import random
import string


def generate_random_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_password = ''.join(random.choices(characters, k=length))
    return random_password


def generate_random_email():
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com']
    random_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    random_domain = random.choice(domains)
    return f'{random_username}@{random_domain}'
