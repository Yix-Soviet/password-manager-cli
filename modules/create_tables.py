from sqlite3 import connect, OperationalError
from modules.selectors_1 import system, os_name, sleep


con = connect(database="database/db.sqlite3", uri=True)
cur = con.cursor()


def create_tables() -> None:
    try:
        cur.execute(
            "CREATE TABLE passwords(id INTEGER PRIMARY KEY AUTOINCREMENT, name CHAR(50), username CHAR(50), password CHAR, url CHAR)"
        )
    except OperationalError:
        print("The table has already been created, skipping ...")
        sleep(3.5)
        system("cls" if os_name == "nt" else "clear")
