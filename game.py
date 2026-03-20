from random import randint
from pathlib import Path
import json

# создаем фиксированные пути
base_path = Path(__file__).resolve().parent
metadata_path = base_path / "metadata" / "data.json"

# загружаем данные
with open(metadata_path, "r", encoding="utf-8") as f:
    metadata = json.load(f)

gen_data = metadata.get("generation_data")
abbreviations_data = metadata.get("abbreviations_data")
data = metadata.get("data")

def help_to_win(user_inp: str) -> str:
    """
    Функция, которая немного подмещивает результаты,
    помогая игроку чаще выигрывать.
    """
    global data
    print("помогаю выиграть.")
    res = data.get(user_inp)
    return res

def winner_selection(user_inp: str, computer_inp: str) -> str:
    """
    Определяет победителя и возвращает фразу.
    """
    global data
    user_data = data.get(user_inp)
    comp_data = data.get(computer_inp)
    print(f"Пользователь - {user_inp}, компьютер - {computer_inp}")
    if user_data == computer_inp:
        return "Выиграл пользователь"
    elif comp_data == user_inp:
        return "Упс, выиграл компьютер"
    else:
        return "Ничья, играем еще раз)"
    

def rps_choise(user_inp: str) -> str:
    """Обрабатывает выбор пользователя и компьютера,
    и выдает результат.
    """
    global randint, gen_data, abbreviations_data
    comp_choise_int = randint(0, 3)
    user_choise = abbreviations_data.get(user_inp) # преобразую сокращения
    comp_choise = gen_data.get(comp_choise_int) # проеобразуем выбор компьютера

    if comp_choise_int == 3:
        comp_choise = help_to_win(user_choise)

    res = winner_selection(user_choise, comp_choise)
    return res

