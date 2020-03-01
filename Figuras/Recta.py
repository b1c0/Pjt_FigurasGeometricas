import math
class Recta:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def longitud(self):
        a = self.x2-self.x1
        b = self.y2-self.y1
        long =  math.sqrt(math.pow(a,2)+math.pow(b,2)) 
        print("mi longitud es: "+str(long))

    def mover(self,x,y):
        dx = self.x1-x
        dy = self.y1-y
        self.x2 = self.x2-dx
        self.y2 = self.y2-dy
        self.x1 = x
        self.y1 = y
        print( "La nueva posicion es: ("+str(self.x1)+", "+str(self.y1)+") ("+str(self.x2)+", "+str(self.y2)+")")