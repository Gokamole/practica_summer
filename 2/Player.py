class Player:
    def __init__ (self,name,level,experience):
        self.name = name
        self.level = level
        self.experience = experience

    def gain_experience(self):
        self.experience = self.experience + int(input("Кол-во опыта: "))
        if self.level == 0:
            if self.experience >= 100:
                self.level =+ 1
        if self.level == 1:
            if self.experience >= 200:
                self.level =+ 1
        if self.level == 2:
            if self.experience >= 400:
                self.level =+ 1
        if self.level == 3:
            if self.experience >= 800:
                self.level =+ 1
        if self.level == 4:
            if self.experience >= 1600:
                self.level =+ 1
        if self.level == 5:
            if self.experience >= 3200:
                self.level =+ 1
        if self.level == 6:
            if self.experience >= 6400:
                self.level =+ 1
        if self.level == 7:
            if self.experience >= 12800:
                self.level =+ 1
        if self.level == 8:
            if self.experience >= 25600:
                self.level =+ 1
        if self.level == 9:
            if self.experience >= 51200:
                self.level =+ 1
    
    def show_stats(self):
        print(self.name)
        print(self.level)
        print(self.experience)
