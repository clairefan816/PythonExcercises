class Point:
    def __init__(self, x, y):
        self.xCoord = x
        self.yCoord = y

    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord

    def midPoint(self, otherPoint):
        newX = lerp(otherPoint.xCoord, self.xCoord, 0.5)
        newY = lerp(otherPoint.yCoord, self.yCoord, 0.5)
        return Point(newX, newY)
