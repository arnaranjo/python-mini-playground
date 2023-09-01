'''
IMG source:
    https://en.wikipedia.org/wiki/Equirectangular_projection
'''

from turtle import RawTurtle, TurtleScreen

class issTrakerTurtle():
    def __init__(self, canvas, issPosition):
        
        self.issPosition = issPosition

        self.screen = TurtleScreen(canvas)
        self.screen.setworldcoordinates(
            llx = -180.0,
            lly = -90.0,
            urx = 180.0,
            ury = 90.0
        )
    
    def setISS(self):
        self.issTurtle = RawTurtle(self.screen)
        self.issTurtle.shape("circle")
        self.issTurtle.penup()
        self.issTurtle.goto(self.issPosition)
        
    def UpdateISSLocation(self, issPosition):
        self.issTurtle.goto(issPosition)
