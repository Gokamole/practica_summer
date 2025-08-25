# Импорт класса
from heptagon import Heptagon

# Главная функция
def main():
    side_length = float(input(f"Введите длину стороны семиугольника: "))  # длина стороны октагона
    heptagon = Heptagon(side_length)
    
    print(f"Радиус описанной окружности: {heptagon.get_radius_circumscribed()}")
    print(f"Площадь описанной окружности: {heptagon.get_area_circumscribed()}")
    print(f"Радиус вписанной окружности: {heptagon.get_radius_inscribed()}")
    print(f"Площадь вписанной окружности: {heptagon.get_area_inscribed()}")
    print(f"Площадь семиугольника: {heptagon.get_area()}")
    print(f"Периметр семиугольника: {heptagon.get_perimeter()}")

    heptagon.draw()  # Визуализация

if __name__ == "__main__":
    main()