from game import rps_choise

# trans_data ={
#     "rock": "камень",
#     "paper": "paper",
#     "scissors": ""
# }

def game():
    check = ["R", "P", "S"]
    while True:
        inp = input("Выбери R - камень, P - бумага, S - ножницы.\n> ")
        if inp.lower() == "exit":
            break
        elif inp.upper() not in check:
            print("Нет так не честно, такого варианта нет.")
        else:
            res = rps_choise(inp)
            print(res)
            if res == "Ничья, играем еще раз)":
                continue
            inp = input("Сыграем еще раз? :) (да или нет)\n> ")
            if inp.lower() == "да":
                continue
            elif inp.lower() == "нет":
                print("Было приятно поиграть с тобой :)")
                break
            else:
                print("Не опнял тебя :(")
                continue

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

