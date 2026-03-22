from game import GameLogic
from animations import loading
import shutil
import encryption
import sys


class AuthManager:
    def registration(self):
        login = input("login: ")
        password = input("password: ")
        res = encryption.register(login, password)
        return res

    def loging(self):
        login = input("login: ")
        password = input("password: ")
        res = encryption.login(login, password)
        return res

    def guest(self):
        encryption.load_current_user("guest")
        return True

class MenuController():
    def __init__(self):
        self.auth = AuthManager()
        self.game_logic = GameLogic()
        self.check = ["R", "P", "S"]
        
    def account_1(self):
        columns, _ = shutil.get_terminal_size()
        auth = self.auth
        data = {
            "reg": auth.registration,
            "log": auth.loging,
            "guest": auth.guest,
            "exit": sys.exit
        }
        messege1 = "Приветствую! Это игра «Камень, ножницы, бумага»"
        messege2 = "Для регистрации введите (reg), для входа — (log). Если вы хотите продолжить играть как гость, введите (guest).\n> "

        centrel_m = messege1.center(columns)
        print(centrel_m)
        while True:
            inp = input(messege2).lower().strip()
            action = data.get(inp)
            
            if action == None:
                print("Не понял тебя... :(")
            else:
                res = action()
                if res == True: # если все успешно, пускаем в игру
                    self.start_menu_2()

    def start_menu_2(self):
        """
        Это стартовое меню, при вводе start запуститься игра.
        """
        messege1 = "Напишите start для начала или exit для выхода из игры.\n> "
        while True:
            inp = input(messege1).lower().strip()
            if inp == 'exit':
                sys.exit()
            elif inp == 'start':
                print("Начинаем игру :)")
                self.game_3()
            else:
                print("Не понял тебя... :(")

    def game_3(self):

        while True:
            inp = input("Выбери R - камень, P - бумага, S - ножницы.\n> ").upper().strip()
            if inp in self.check:
                loading()

                res = self.game_logic.rps_choise(inp)
                print(res)

                if res == "Ничья, играем еще раз)":
                    continue
                else:
                    self.game_4()
                if inp == "no":
                    break
            elif inp == "EXIT":
                sys.exit()
            else:
                print("Нет так не честно, такого варианта нет.")

    def game_4(self):
        global inp
        while True:
            inp = input("Сыграем еще раз? :) (yes or no)\n> ").lower().strip()
            if inp == "yes":
                break
            elif inp == "no":
                print("Было приятно поиграть с тобой :)")
                break
            else:
                print("Не опнял тебя :(")


if __name__ == "__main__":
    game = MenuController()
    game.account_1()

