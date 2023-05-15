from modules.encrypt_passwd import encrypt_passwd, decrypt_passwd
from modules.add_passwords import add_password
from modules.create_tables import cur
from modules.selectors_1 import verify_selection, system, os_name, sleep


def add_passwd_menu() -> None:
    while True:
        system("cls" if os_name == "nt" else "clear")
        print("--- Add Password ---")
        name = str(input("Enter a name to identify the key: "))
        username = str(input("Enter the username: "))
        password = str(input("Enter thr password: "))
        url = str(input("Insert the URL: "))
        check = verify_selection("Do you want to save this password? [YES/Y or NO/N]")

        if check.capitalize() in ["NO", "N"]:
            print("Reloading form ...")
            sleep(3)
            system("cls" if os_name == "nt" else "clear")
        elif check.capitalize() in ["YES", "Y"]:
            break

    encrypted_password = encrypt_passwd(password)

    try:
        add_password(name, username, encrypted_password, url)
    except:
        print("An error occurred while adding the password.")


def view_passwd_menu() -> None:
    passwords = cur.execute("SELECT * FROM passwords").fetchall()

    print("--- View Passowrds ---")

    for password in passwords:
        decrypted_password = decrypt_passwd(password[3])
        print(
            f"| Name: {password[1]} | Username: {password[2]} | Password: {decrypted_password} | URL: {password[4]} |"
        )
