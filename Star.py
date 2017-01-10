class star:
    def __init__(self,Position):
        self.x , self.y = Position
        self.velosity = 0
        self.radius = 5
        self.mass = 100

    def getPosition(self):
        return self.x , self.y

    def setPosition(self , NewPosition):
        self.x, self.y = NewPosition

    def setVelosity(self,Velosity):
        self.velosity = Velosity

    def getMass(self):
        return self.mass
    
    def getVelosity(self):
        return self.velosity