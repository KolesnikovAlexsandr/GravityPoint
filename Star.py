import Physics
import math
class star:
    def __init__(self,Position):
        self.x , self.y = Position
        self.vX = 0
        self.vY = 0
        self.radius = 5
        self.mass = 100
        self.aX = 0
        self.aY = 0


    def getPosition(self):
        return self.x , self.y

    def setPosition(self , NewPosition):
        self.x, self.y = NewPosition

    def setVelosity(self,Velosity):
        self.vX = Velosity[0]
        self.vY = Velosity[1]

    def setMass(self , mass):
        self.mass = mass

    def getMass(self):
        return self.mass

    def getVelosity(self):
        return self.vX , self.vY

    def CalculateVelosity(self , StarList , i):
        j = 0
        d = 0
        while j < len(StarList):
            if(i != j):
                d = math.sqrt((self.x - StarList[j].getPosition()[0])*(self.x - StarList[j].getPosition()[0]) +
                              (self.y - StarList[j].getPosition()[1])*(self.y - StarList[j].getPosition()[1]))
                self.vX += (Physics.GetGravityConst()*StarList[j].getMass()/(d*d))*((StarList[j].getPosition()[0] - self.x)/d)
                self.vY += (Physics.GetGravityConst() * StarList[j].getMass() / (d * d)) * (
                (StarList[j].getPosition()[1] - self.y) / d)
            j = j + 1

    def CalculatePosition(self,border):
        self.x +=self.vX
        self.y +=self.vY
        self.x = int( self.x )
        self.y = int( self.y )




