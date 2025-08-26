from exercise_1 import Ex_1
from exercise_2 import Ex_2
from exercise_3 import Ex_3
from exercise_3 import Ex3


def menu():
    print("Выберите программу для запуска:")
    print("1 — Ограничение числа одновременных потоков")
    print("2 — Обработка больших файлов")
    print("3 — Синхронизация")
    choice = input("Ваш выбор: ")

    if choice == '1':
        Ex1 = Ex_1(5)
        Ex1.zamer_vremeni(100)
    elif choice == '2':
        files = ["f1.txt", "f2.txt", "f3.txt", "f4.txt"]
        Ex2 = Ex_2(files)
        Ex2.posled()
        Ex2.parallel()
        Ex2.results()
    elif choice == '3':
        Ex3()
    else:
        print("Пока в разработке")

if __name__ == "__main__":
    menu()
