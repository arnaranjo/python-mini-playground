import time
from turtle import Screen
from snake import Snake

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GAME = True

screen = Screen()
screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game!")

screen.tracer(0)

newSnake = Snake()

while GAME:
    screen.update()
    time.sleep(0.1)
    newSnake.MoveSnake()

screen.mainloop()