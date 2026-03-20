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
    помогая игроку чаще выигрывать.
    """
    print("помогаю выиграть.")
    res = data2.get(user_inp)
    return res

def winner_selection(user_inp: str, computer_inp: str) -> str:
    """Бдует определять кто выиграл и формировать строку на вывод."""
    user_data = data2.get(user_inp)
    comp_data = data2.get(computer_inp)
    print(f"Пользователь - {user_inp}, компьютер - {computer_inp}")
    if user_data == computer_inp:
        return "Выиграл пользователь"
    elif comp_data == user_inp:
        return "Упс, выиграл компьютер"
    else:
        return "Ничья, играем еще раз)"
    

def rps_choise(user_inp: str) -> str:
    """Обрабатывает вывбор пользователя и компьютера,
    и выдает результат.
    """
    global randint, data, trans_data
    comp_choise = randint(0, 3)
    user_choise = trans_data.get(user_inp) # преобразую сокращения
    comp_choise = data.get(comp_choise) # проеобразуем выбор компьтера

    if comp_choise == 3:
        help_to_win(user_choise)
    else:
        res = winner_selection(user_choise, comp_choise)
    return res

