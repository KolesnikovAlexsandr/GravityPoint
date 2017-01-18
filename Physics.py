
def getCenterOfMassPosition(StarMass):
    xPosition = 0
    yPosition = 0
    AllMass = 0
    i = 0
    while i < len(StarMass):
        xPosition = xPosition + StarMass[i].getPosition()[0]*StarMass[i].getMass()
        yPosition = yPosition + StarMass[i].getPosition()[1]*StarMass[i].getMass()
        AllMass = AllMass + StarMass[i].getMass()
        i = i +1
    xPosition = xPosition/AllMass
    yPosition = yPosition/AllMass
    return xPosition , yPosition


def getAllMass(StarMass):
    AllMass = 0
    i = 0
    while i < len(StarMass):
        AllMass = AllMass + StarMass[i].getMass()
        i = i +1
    return AllMass


def GetGravityConst():
    return 5