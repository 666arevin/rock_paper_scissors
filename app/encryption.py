import hashlib
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
user_data_p = BASE_DIR / "data" / "user_data.json"

def register(user_name: str, password: str):
    """
    Производит регистрацию нового пользователя.
    Args:
        user_name (str): имя пользователя
        password (str): пароль пользователя
    """
    global user_data_p
    hash_p = hashlib.sha224(password.encode()).hexdigest()
    
    with open(user_data_p, "r", encoding="utf-8") as f:
        data = json.load(f)

    if user_name in data:
        return "Пользователь с таким именем уже существует."
    else:
        data[user_name] = hash_p

    with open(user_data_p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    inp = input("Желаете произвести автоматический вход под этими данными? (yes or no)").lower().strip()
    if inp == "yes":
        login()
    else:
        # возможно, нужно возвращать данные от аккаунта
        return "Вы были успешно зарегестрированы."
    

def login(user_name: str, password: str):
    global user_data_p
    hash_p = hashlib.sha224(password.encode()).hexdigest()
    
    with open(user_data_p, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if user_name in data:
        password = data[user_name]
        if password == hash_p:
            pass
            # успешно вошли
    else:
        return "Пользователя с таким именем не существует."