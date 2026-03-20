from random import randint
from pathlib import Path
import json


class GameLogic():
    def __init__(self):
        # создаем фиксированные пути
        base_path = Path(__file__).resolve().parent
        metadata_path = base_path / "metadata" / "data.json"

        # загружаем данные
        with open(metadata_path, "r", encoding="utf-8") as f:
            metadata = json.load(f)

        self.gen_data = metadata.get("generation_data")
        self.abbreviations_data = metadata.get("abbreviations_data")
        self.data = metadata.get("data")

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
        Определяет победителя и возвращает фразу.
        """
        user_data = self.data.get(user_inp)
        comp_data = self.data.get(computer_inp)
        print(f"Пользователь - {user_inp}, компьютер - {computer_inp}")
        if user_data == computer_inp:
            return "Выиграл пользователь"
        elif comp_data == user_inp:
            return "Упс, выиграл компьютер"
        else:
            return "Ничья, играем еще раз)"
        

    def rps_choise(self, user_inp: str) -> str:
        """Обрабатывает выбор пользователя и компьютера,
        и выдает результат.
        """
        comp_choise_int = str(randint(0, 3))
        user_choise = self.abbreviations_data.get(user_inp) # преобразую сокращения
        comp_choise = self.gen_data.get(comp_choise_int) # проеобразуем выбор компьютера

        if comp_choise_int == 3:
            comp_choise = self.help_to_win(user_choise)

        res = self.winner_selection(user_choise, comp_choise)
        return res

