class Player:
    def __init__ (self,name,level,experience):
        self.name = name
        self.level = level
        self.experience = experience

    def gain_experience(self):
        self.experience = self.experience + int(input("Кол-во опыта"))
        if self.experience >= 100:
            self.level =+ 1

