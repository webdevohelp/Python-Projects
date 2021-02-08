
class car():
    def __init__(self, color, wheels):
        self.color = color
        self.wheels = wheels
    def __str__(self) -> str:
        return f"The color of car is : {self.color}\nThe number of wheels is {self.wheels}"
car1 = car("red",4)