from Player import Player
from Player import Warrior

player = Player("Плэер", 0, 0)
player.gain_experience()
player.show_stats()

warrior = Warrior("Вариор", 0, 0, 50, 50)
warrior.gain_experience()
warrior.show_stats()
warrior.attack()
warrior.defend()
warrior.show_info()