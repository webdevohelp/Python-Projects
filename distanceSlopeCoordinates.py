class Line:
    #program to calculate the distance between two coordinates and slope of the line
    def __init__(self, coor1, coor2):
        self.coor1 = coor1
        self.coor2 = coor2
        self.coor1x = coor1[0]
        self.coor1y = coor1[1]
        self.coor2x = coor2[0]
        self.coor2y = coor2[1]
    def distance(self):
        return (((self.coor2x - self.coor1x)**2) + ((self.coor2y - self.coor1y)**2))**0.5
    def slope(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2 
        return (y2-y1)/(x2-x1)

c1 = (3,2)
c2 = (8,10)
myline = Line(c1,c2)
print(myline.distance())
print(myline.slope())