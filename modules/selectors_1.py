from os import system
from os import name as os_name
from time import sleep

def verify_selection(text_input: str) -> str:
    while True:
        var_input = str(input(text_input))
        if var_input.capitalize() not in ["YES", "Y", "NO", "N"]:
            print("Incorrect input, please try again")
        else:
            break

    return var_input

def selector_menu(text_input: str, second_text: str, func) -> None:
    while True:
        func()
        go_back = verify_selection(text_input)
        if go_back.capitalize() in ["NO", "N"]:
            system("cls" if os_name == "nt" else "clear")
        elif go_back.capitalize() in ["YES", "Y"]:
            print(second_text)
            sleep(2)
            system("cls" if os_name == "nt" else "clear")
            break