import time
import sys

def loading():
    print("Загрузка", end="")
    for i in range(10):
        print(".", end="")
        sys.stdout.flush()
        time.sleep(0.3)
    print(" Готово!")
