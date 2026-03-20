from game import GameLogic
from animations import loading

# trans_data ={
#     "rock": "камень",
#     "paper": "paper",
#     "scissors": ""
# }
game_logic = GameLogic()
def game():
    global game_logic
    check = ["R", "P", "S"]
    while True:
        inp = input("Выбери R - камень, P - бумага, S - ножницы.\n> ")
        if inp.lower() == "exit":
            break
        elif inp.upper() not in check:
            print("Нет так не честно, такого варианта нет.")
        else:
            loading()
            res = game_logic.rps_choise(inp)
            print(res)
            if res == "Ничья, играем еще раз)":
                continue
            while True:
                inp = input("Сыграем еще раз? :) (yes or no)\n> ")
                if inp.lower() == "yes":
                    break
                elif inp.lower() == "no":
                    print("Было приятно поиграть с тобой :)")
                    break
                else:
                    print("Не опнял тебя :(")
                    continue
            if inp.lower() == "no":
                break

def start_menu():
    """
    Это стартовое меню, при вводе start запуститься игра.
    """
    while True:
        inp = input("Хотите сыграть в камень ножницы бумага? Напишите start для начала или exit для выхода.\n> ")
        if inp == 'exit':
            break
        elif inp == 'start':
            print("Начинаем игру :)")
            game()
            break
        else:
            print("Не знаю такую команду...")

if __name__ == "__main__":
    start_menu()

