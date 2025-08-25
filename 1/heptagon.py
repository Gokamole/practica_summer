# Импорт нужных библиотек
import math
import matplotlib.pyplot as plt


# Класс для семиугольника
class Heptagon:

    # Конструктор
    def __init__(self, side_length):
        self.side_length = side_length
        self.angle = 2*math.pi / 7  # угол семиугольника
        
    # Радиус описанной окружности
    def get_radius_circumscribed(self):
        return self.side_length/(2*math.sin(math.pi / 7))

    # Площадь описанной окружности
    def get_area_circumscribed(self):
        radius = self.get_radius_circumscribed()
        return (math.pi * (radius ** 2))
    
    # Радиус вписанной окружности
    def get_radius_inscribed(self):
        return self.side_length / (2* math.tan(math.pi/7))

    # Площадь вписанной окружности
    def get_area_inscribed(self):
        radius1 = self.get_radius_inscribed()
        return (math.pi * (radius1 ** 2))

    # Собственная площадь
    def get_area(self):
        return (7 * (self.side_length ** 2))/(4 * math.tan(math.pi/7))

    # Собственный периметр
    def get_perimeter(self):
        return 7 * self.side_length
    
    # Визуализация
    def draw(self):
        fig, ax = plt.subplots(figsize=(15, 15))
        ax.set_aspect('equal')

        R_out = self.get_radius_circumscribed()
        R_in = self.get_radius_inscribed()

        # координаты вершин семиугольника
        x = [R_out * math.cos(2 * math.pi * i / 7) for i in range(7)]
        y = [R_out * math.sin(2 * math.pi * i / 7) for i in range(7)]

        ax.fill(x, y, color='black', label='Семиугольник')

        # описанная окружность
        circle_circ = plt.Circle((0, 0), R_out, color="blue", fill=False, label="Описанная окружность")
        ax.add_patch(circle_circ)

        # вписанная окружность
        circle_in = plt.Circle((0, 0), R_in, color="red", fill=False, label="Вписанная окружность")
        ax.add_patch(circle_in)

        plt.legend()
        plt.grid()
        plt.show()
    
    # Деструктор
    def __del__(self):
        pass