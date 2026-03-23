from pathlib import Path
import json
import random
import shutil

BASE_DIR = Path(__file__).resolve().parent
score_path = BASE_DIR / "data" / "scores.json"

class ScoreBoard:
    def __init__(self):
        
        self.user = None # текущий пользователь
    def load_data(self):
        """
        Загружате актуальные данные.
        """
        with open(score_path, "r", encoding="utf-8") as f:
            self.data = json.load(f)

    def user_stat(self) -> None:
        """
        Функция выводит количество выигрышей, ничьих и проигрышей.
        """
        self.load_data()
        if self.user == "guest":
            print("Авторизуйтись, чтобы смотреть статистику")
            return
        scores = self.data[self.user]
        messages = ["Выигрышей: ", "Ничья: ", "Проигрышей: "]
        res = [scores.count(1), scores.count(0), scores.count(-1)]
        for mes, scor in zip(messages, res):
            print(mes + str(scor))
    
    def graphical_stat(self) -> None:
        """
        Выводит график ваших побед.
        """
        self.load_data()
        if self.user == "guest":
            print("Авторизуйтись, чтобы смотреть статистику")
            return
        columns, _ = shutil.get_terminal_size()
        total = 0
        points = []
        messege = "Динамика ваших побед в игре «Камень, ножницы, бумага»."
        centrel_m = messege.center(columns)

        for i in self.data[self.user]:
            if i == 1:
                total += 1
            points.append(total)
        max_height = max(points) if points else 0

        print(centrel_m)
        for p in range(max_height, 0, -1):
            line = ""
            for i in points:
                line += "* " if i == p else "  "
            print(f"| {line}")
        
        print(f"| {"- " * len(points)}")

    def reset_points(self) -> None:
        """
        Сбрасывает результаты конкретного пользователя
        """
        self.load_data()
        if self.user == "guest":
            print("Авторизуйтись, чтобы смотреть статистику")
            return
        self.data[self.user] = []
        with open(score_path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4)
        print("Успешно.")
        
    def current_user(self) -> None:
        print(self.user)
            

