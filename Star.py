import Physics
import math
class star:
    def __init__(self,Position):
        self.x , self.y = Position
        self.velosity = 0
        self.radius = 5
        self.mass = 100
        self.acceleration = 0
        self.xAngle = 0
        self.yAngle = 0

    def getPosition(self):
        return self.x , self.y

    def setPosition(self , NewPosition):
        self.x, self.y = NewPosition

    def setVelosity(self,Velosity):
        self.velosity = Velosity

    def setMass(self , mass):
        self.mass = mass

    def getMass(self):
        return self.mass

    def getVelosity(self):
        return self.velosity

    def CalculateAcceleration(self , CenterOfMass):
        xLen = self.x - CenterOfMass.getPosition()[0]
        yLen = self.y - CenterOfMass.getPosition()[1]
        hypotenuse = math.sqrt(xLen*xLen + yLen*yLen)
        if hypotenuse < 10:
            self.velosity = 0
            self.acceleration = 0
        else:
            self.acceleration = (Physics.GetGravityConst()*CenterOfMass.getMass())/(hypotenuse * hypotenuse)
            self.xAngle = xLen / hypotenuse
            self.yAngle = yLen / hypotenuse



    def CalculatePosition(self):
        self.velosity = (self.velosity + self.acceleration)%50
        self.x = self.x - int(self.velosity*self.xAngle)
        self.y = self.y - int(self.velosity * self.yAngle)



