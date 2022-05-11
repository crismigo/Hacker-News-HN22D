import random
import string


def generate_key():
    chars = ''.join([string.ascii_letters, string.digits, string.punctuation]).replace('\'', '').replace('"','').replace('\\', '')

    SECRET_KEY = ''.join([random.SystemRandom().choice(chars) for i in range(32)])
    return SECRET_KEY


print(generate_key())