from modules.create_tables import create_tables
from modules.views import add_passwd_menu, view_passwd_menu
from modules.selectors_1 import selector_menu, sleep, system, os_name


create_tables()
menu_title = """
#  _____                               _  __  __                                         
# |  __ \                             | ||  \/  |                                        
# | |__) |__ _  ___  ___ __      __ __| || \  / |  __ _  _ __    __ _   __ _   ___  _ __ 
# |  ___// _` |/ __|/ __|\ \ /\ / // _` || |\/| | / _` || '_ \  / _` | / _` | / _ \| '__|
# | |   | (_| |\__ \\\__ \ \ V  V /| (_| || |  | || (_| || | | || (_| || (_| ||  __/| |   
# |_|    \__,_||___/|___/  \_/\_/  \__,_||_|  |_| \__,_||_| |_| \__,_| \__, | \___||_|   
#                                                                       __/ |            
#                                                                      |___/             
----------------------------------------------------------------------------------------

  * View Passwords (1)
  * Add password (2)
  * Exit (q)
"""

while True:
    print(menu_title)
    selection = str(input("Select what you want to do: "))

    if selection not in ["1", "2", "q"]:
        print("Incorrect entry, select again ...")
        sleep(2)
        system("cls" if os_name == "nt" else "clear")
    else:
        if selection == "1":
            system("cls" if os_name == "nt" else "clear")
            selector_menu("Do you want to go back? [YES/Y or NO/N]", "Returning ...", view_passwd_menu)

        if selection == "2":
            system("cls" if os_name == "nt" else "clear")
            selector_menu("Do you want to go back? [YES/Y or NO/N]", "Returning ...", add_passwd_menu)

        if selection == "q":
            system("cls" if os_name == "nt" else "clear")
            print("Leaving ...")
            sleep(2)
            exit(0)
