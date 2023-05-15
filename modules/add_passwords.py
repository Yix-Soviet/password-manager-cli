from modules.create_tables import create_tables as con
from modules.create_tables import con, cur


def add_password(name: str, username: str, hashed_password: hash, url: str) -> None:

    cur.execute(f"INSERT INTO passwords(name, username, password, url) VALUES ('{name}', '{username}', '{hashed_password}', '{url}')")
    con.commit()

    print(f"Password with name {name} has been added")