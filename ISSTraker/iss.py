'''
IMG source:
    https://en.wikipedia.org/wiki/Equirectangular_projection
'''

from turtle import RawTurtle, TurtleScreen

class issTrakerTurtle():
    def __init__(self, canvas, issPosition):
        
        self.issPosition = issPosition

        self.screen = TurtleScreen(canvas)
        self.screen.register_shape("ISSTraker/space-station.gif")
        self.screen.setworldcoordinates(
            llx = -180.0,
            lly = -90.0,
            urx = 180.0,
            ury = 90.0
        )
        self.screen.tracer(0)
    
    def setISS(self):
        self.issTurtle = RawTurtle(self.screen)
        self.issTurtle.shape("ISSTraker/space-station.gif")
        self.issTurtle.penup()
        self.issTurtle.goto(self.issPosition)
        self.screen.update()
        
    def UpdateISSLocation(self, issPosition):
        self.issTurtle.goto(issPosition)
        self.screen.update()