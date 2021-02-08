class Cylinder:
    
    def __init__(self,height=1,radius=1):
        self.h = height
        self.r = radius
        
    def volume(self):
        return 3.14 * (self.r**2) * self.h
    
    def surface_area(self):
        return (3.14 * 2 * self.r * self.h) + 2 * 3.14 * (self.r**2)

mycil = Cylinder(2,3)
print(mycil.volume())
print(mycil.surface_area())