from game import GameLogic
from animations import loading
import shutil
import encryption
import sys
import scoreboard


class AuthManager():
    def __init__(self, game_logic, stat):
        self.game_logic = game_logic
        self.stat = stat

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
        print("Вы успешно вошли)")
        return True
    
    def user_initialization(self):
        cur_user = encryption.load_current_user()
        self.game_logic.current_user = cur_user
        self.stat.user = cur_user

class MenuController():
    def __init__(self):
        self.game_logic = GameLogic()
        self.stat = scoreboard.ScoreBoard()
        self.auth = AuthManager(self.game_logic, self.stat)
        self.check = ["R", "P", "S"]
    
    def account_1(self) -> None:
        """
        Это начальное меню, вход в аккаунт. Без авторизации нельзя
        запустить игру.
        """
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
                auth.user_initialization() # запоминаем кто играет сейчас
                if res == True: # если все успешно, пускаем в игру
                    self.start_menu_2()

    def start_menu_2(self) -> None:
        """
        Это второй уровень, можно запустить игру, выйти из нее или перейти в профиль.
        """
        messege1 = "Напишите start для начала или exit для выхода из игры. profile для входа в профиль.\n> "
        while True:
            inp = input(messege1).lower().strip()
            if inp == 'exit':
                sys.exit()
            elif inp == 'start':
                print("Начинаем игру :)")
                self.game_3()
            elif inp == 'profile':
                self.profile()
            else:
                print("Не понял тебя... :(")

    def game_3(self) -> None:
        """
        Третий уровень, сама игра.
        """
        while True:
            self.inp = input("Выбери R - камень, P - бумага, S - ножницы.\n> ").upper().strip()
            if self.inp in self.check:
                loading()

                res = self.game_logic.rps_choise(self.inp)
                print(res)

                if res == "Ничья, играем еще раз)":
                    continue
                else:
                    self.game_4()
                    if self.inp == "no":
                        break
            elif self.inp == "EXIT":
                sys.exit()
            else:
                print("Нет так не честно, такого варианта нет.")

    def game_4(self):
        """
        Меню выбора после выигрыша или проигрыша.
        """
        while True:
            self.inp = input("Сыграем еще раз? :) (yes or no)\n> ").lower().strip()
            if self.inp == "yes":
                break
            elif self.inp == "no":
                print("Было приятно поиграть с тобой :)")
                break
            else:
                print("Не опнял тебя :(")
        
    def profile(self):
        data = {
            "user": self.stat.current_user,
            "stat": self.stat.user_stat,
            "stat_grap": self.stat.graphical_stat,
            "reset": self.stat.reset_points,
            "exit": sys.exit
        }
        messege2 = "Вам доступны следующий функции (back для выхода):\nuser - текущий пользователь\nstat/stat_grap - просмотр статистики\nreset - сброс результатов."
        print(messege2)
        while True:
            inp = input("> ").lower().strip()
            if inp == 'back':
                break
            action = data.get(inp)
            if action == None:
                print("Не опнял тебя :(")
            else:
                action()


if __name__ == "__main__":
    game = MenuController()
    game.account_1()

