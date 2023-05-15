from cryptography.fernet import Fernet
from os import getenv
from dotenv import load_dotenv


load_dotenv()


def encrypt_passwd(passwd: str) -> str:
    key = getenv("FERNET_KEY")
    f = Fernet(key)
    encrypted_password = f.encrypt(passwd.encode("utf8"))

    return encrypted_password.decode("utf8")


def decrypt_passwd(passwd: str) -> str:
    key = getenv("FERNET_KEY")
    f = Fernet(key)
    decrypted_password = f.decrypt(passwd.encode("utf8"))

    return decrypted_password.decode("utf8")
