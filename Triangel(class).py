class Triangel():
    number_of_sides = 3
    def __init__(self, angel1, angel2, angel3):
        self.angel1 = angel1
        self.angel2 = angel2
        self.angel3 = angel3
    def check_angels(self):
        if self.angel1+self.angel2+self.angel3 == 180:
            return True
        else:
            return False
