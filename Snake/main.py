import time
from turtle import Screen
from snake import Snake
from fruit import Fruit

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

KEY_UP = "Up"
KEY_LEFT = "Left"
KEY_DOWN = "Down"
KEY_RIGHT = "Right"

GAME = True

screen = Screen()
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game!")

screen.tracer(0)
screen.listen()

newSnake = Snake()
newFruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.onkeypress(newSnake.UpSnake, KEY_UP)
screen.onkeypress(newSnake.LeftSnake, KEY_LEFT)
screen.onkeypress(newSnake.DownSnake, KEY_DOWN)
screen.onkeypress(newSnake.RightSnake, KEY_RIGHT)

while GAME:
    screen.update()    
    time.sleep(0.1)

    newSnake.MoveSnake()

    if newSnake.snakeHead.distance(newFruit.currentFruit) < 15:
        newFruit.GenPosition()
        newSnake.CreateBodyElement()
        print("Tocado")

    

screen.mainloop()