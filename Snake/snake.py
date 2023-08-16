from turtle import Turtle

INIT_POSITION = [(-20 ,0), (-41 ,0), (-62 ,0)]

class Snake():
    def __init__(self):
        
        self.snakeBody : Turtle = []
        self.Position()
        self.MoveSnake()

    def Position(self):
        for i in INIT_POSITION:
            bodyElement = Turtle("square")
            bodyElement.penup()
            bodyElement.color("white")
            bodyElement.setpos(i)
            self.snakeBody.append(bodyElement)
    
    def MoveSnake(self):
        for element in self.snakeBody:
            element.forward(21)
