from random import randint
from pathlib import Path
import json


class GameLogic():
    """
    Логика игры.
    """
    def __init__(self):
        # создаем фиксированные пути
        base_path = Path(__file__).resolve().parent
        metadata_path = base_path / "metadata" / "data.json"
        self.score_data_p = base_path / "data" / "scores.json"

        # загружаем данные
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)

        self.gen_data = metadata.get("generation_data")
        self.abbreviations_data = metadata.get("abbreviations_data")
        self.data = metadata.get("data")
        self.tranlate_data = metadata.get("en_ru_trans")

        self.current_user = None
        self.points = None

    def help_to_win(self, user_inp: str) -> str:
        """
        Функция, которая немного подмещивает результаты,
        помогая игроку чаще выигрывать.
        """
        print("помогаю выиграть.")
        res = self.data.get(user_inp)
        return res

    def winner_selection(self, user_inp: str, computer_inp: str) -> str:
        """
        Определяет победителя, сохраняет результаты, возвращает фразу.
        Args:
            user_inp (str): Выбор пользователя
            computer_inp (str): Выбор екомпьютера
        Входные данные на английском, название выбранного предмета.
        """
        user_data = self.data.get(user_inp)
        comp_data = self.data.get(computer_inp)
        print(f"Пользователь - {user_inp}, компьютер - {computer_inp}")
        if user_data == computer_inp:
            self.save_game_res(1)
            return "Выиграл пользователь"
        elif comp_data == user_inp:
            self.save_game_res(-1)
            return "Упс, выиграл компьютер"
        else:
            self.save_game_res(0)
            return "Ничья, играем еще раз)"
        
    def winner_selection_nosave(self, user_inp, computer_inp) -> str:
        """
        Определяет победителя и возвращает фразу. НЕ сохарняет рехультаты.
        Args:
            user_inp (str): Выбор пользователя
            computer_inp (str): Выбор екомпьютера
        Входные данные на английском, название выбранного предмета.
        """
        user_data = self.data.get(user_inp)
        comp_data = self.data.get(computer_inp)
        user_inp_ru = self.tranlate_data.get(user_data)
        computer_inp_ru = self.tranlate_data.get(comp_data)
        
        print(f"Ты выбрал - {user_inp_ru}, я выбрал - {computer_inp_ru}.")
        if user_data == computer_inp:
            return "Выиграл пользователь"
        elif comp_data == user_inp:
            return "Упс, выиграл компьютер"
        else:
            return "Ничья, играем еще раз)"
        
    def rps_choise(self, user_inp: str) -> str:
        """
        Обрабатывает выбор пользователя и компьютера
        Args:
            user_inp (str): выбор пользователя.
        """
        comp_choise_int = str(randint(0, 3))
        user_choise = self.abbreviations_data.get(user_inp) # преобразую сокращения
        comp_choise = self.gen_data.get(comp_choise_int) # проеобразуем выбор компьютера
        
        if comp_choise_int == "3":
            comp_choise = self.help_to_win(user_choise)
        if self.current_user == "guest":
            res = self.winner_selection_nosave(user_choise, comp_choise)
        else:
            res = self.winner_selection(user_choise, comp_choise)
        return res
    
    def save_game_res(self, point: int) -> None:
        """
        Сохраняет результаты текущий игры.
        Args:
            point (int): очки.
        """
        with open(self.score_data_p, "r", encoding="utf-8") as f:
            data = json.load(f)
        data[self.current_user].append(point)

        with open(self.score_data_p, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

