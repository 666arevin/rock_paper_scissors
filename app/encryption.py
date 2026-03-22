import hashlib
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
user_data_p = BASE_DIR / "data" / "user_data.json"

# переменная для определеннея текщего пользователя
current_user = None 

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
        print("Пользователь с таким именем уже существует.")
        return False
    else:
        data[user_name] = hash_p

    with open(user_data_p, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    inp = input("Желаете произвести автоматический вход под этими данными? (yes or no)\n> ").lower().strip()
    if inp == "yes":
        login()
    else:
        print("Вы были успешно зарегестрированы.")
        return True


def login(user_name: str, password: str):
    global user_data_p, current_user
    hash_p = hashlib.sha224(password.encode()).hexdigest()
    
    with open(user_data_p, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if user_name in data:
        password = data[user_name]
        if password == hash_p:
            current_user = user_name
            print("Успешная авторизация.")
            return True
        else:
            print("Пароль неверный")
            return False
    else:
        print("Пользователя с таким именем не существует.")
        return False

def load_current_user(user_name: str):
    global current_user
    current_user = user_name
    print("Вы успешно вошли)")
    return True