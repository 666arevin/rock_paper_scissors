import hashlib
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent
user_data_p = BASE_DIR / "data" / "user_data.json"
score_data_p = BASE_DIR / "data" / "scores.json"

# переменная для определеннея текщего пользователя

current_user = "guest"

def register(user_name: str, password: str):
    """
    Производит регистрацию нового пользователя.
    Args:
        user_name (str): имя пользователя
        password (str): пароль пользователя
    """
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
        login(user_name, password)
    else:
        print("Вы были успешно зарегестрированы.")
        return True


def login(user_name: str, password: str):
    global current_user
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


def load_current_user():
    return current_user

def check_scores():
    with open(user_data_p, "r", encoding="utf-8") as f:
        users_data = json.load(f)

    with open(score_data_p, "r", encoding="utf-8") as f:
        scores_data = json.load(f)
    
    for i in users_data.keys():
        if i not in scores_data:
            scores_data[i] = []
    
    with open(score_data_p, "w", encoding="utf-8") as f:
        json.dump(scores_data, f, indent=4, ensure_ascii=False)

check_scores()