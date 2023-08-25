from turtle import Turtle

INIT_POSITION = [(-20 ,0), (-40 ,0), (-60 ,0)]
DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self,snakeColor):
        
        self.snakeColor = snakeColor
        self.snakeBody :Turtle = []
        self.CreateSnake()
        self.snakeHead = self.snakeBody[0]
        self.MoveSnake()

    def CreateBodyElement(self, position):
        bodyElement = Turtle("square")
        bodyElement.penup()      
        bodyElement.color(self.snakeColor)
        bodyElement.setpos(position)
        self.snakeBody.append(bodyElement)

    def CreateSnake(self):
        for position in INIT_POSITION:
            self.CreateBodyElement(position)                           
    
    def AddBodyElement(self):
        self.CreateBodyElement(self.snakeBody[len(self.snakeBody)-1].pos())     
    
    def MoveSnake(self):
        for element in range(len(self.snakeBody)-1, 0, -1):
            newX = self.snakeBody[element - 1].xcor()
            newY = self.snakeBody[element - 1].ycor()
            self.snakeBody[element].goto(newX, newY)
        self.snakeHead.forward(DISTANCE)
    
    def RemoveSnake(self):
        for element in self.snakeBody:
            element.reset()
            element.hideturtle()
        self.snakeBody.clear()

    def RestartSnake(self):
        self.RemoveSnake()
        self.CreateSnake()
        self.snakeHead = self.snakeBody[0]

    def UpSnake(self):
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(UP)

    def LeftSnake(self):
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(LEFT)

    def DownSnake(self):
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(DOWN)

    def RightSnake(self):
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(RIGHT)