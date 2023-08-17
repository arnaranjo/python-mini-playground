from turtle import Turtle

INIT_POSITION = [(-20 ,0), (-41 ,0), (-62 ,0)]
DISTANCE = 21

class Snake():
    def __init__(self):
        
        self.snakeBody = []
        self.Position()
        self.MoveSnake()

    def Position(self):
        for ps in INIT_POSITION:
            bodyElement = Turtle("square")
            bodyElement.penup()
            bodyElement.color("white")
            bodyElement.setpos(ps)
            self.snakeBody.append(bodyElement)
    
    def MoveSnake(self):
        for element in range(len(self.snakeBody)-1, 0, -1):
            newX = self.snakeBody[element - 1].xcor()
            newY = self.snakeBody[element - 1].ycor()
            self.snakeBody[element].goto(newX, newY)
        self.snakeBody[0].forward(DISTANCE)

    def UpSnake(self):
        self.snakeBody[0].setheading(90)

    def LeftSnake(self):
        self.snakeBody[0].setheading(180)

    def DownSnake(self):
        self.snakeBody[0].setheading(270)

    def RightSnake(self):
        self.snakeBody[0].setheading(0)