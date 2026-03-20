from random import randint

data = {
    0: "rock",
    1: "paper",
    2: "scissors"
}
trans_data = {
    "R": "rock",
    "P": "paper",
    "S": "scissors"
}
en_ru_trans = {
    "rock": "камень",
    "paper": "paper",
    "scissors": "ножницы"
}


data2 = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

def help_to_win(user_inp: str) -> None:
    """
    Функция, которая немного подмещивает результаты,
    помогая игроку чащевыигрывать
    """
    print("помогаю выиграть.")
    res = data2.get(user_inp)
    return res

def winner_selection(user_inp: str, computer_int: str) -> str:
    """Бдует определять кто выиграл и формировать строку на вывод."""
    user_data = data2.get(user_inp)
    comp_data = data2.get(computer_int)
    # if user_data == computer_int

def rps_choise(user_inp: str) -> str:
    global randint, data, trans_data
    computer_choise = randint(0, 3)
    user_choise = trans_data.get(user_inp)

    if computer_choise == 3:
        res = data2.get(user_choise)
    else:
        res = data.get(computer_choise)
    res = f""
    return res

