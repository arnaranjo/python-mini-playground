import time
from turtle import Screen
from snake import Snake
from fruit import Fruit
from display import Display

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BORDER = 60

TOP_LIMIT = SCREEN_HEIGHT/2 - BORDER
BOTTOM_LIMIT = -SCREEN_HEIGHT/2 + BORDER
LEFT_LIMIT = -SCREEN_WIDTH/2 + BORDER
RIGHT_LIMIT = SCREEN_WIDTH/2 - BORDER

BACKGROUND_COLOR = "#001d2a"
SNAKE_COLOR = "#00be91"
FRUIT_COLOR = "#9af089"
DISPLAY_COLOR = "#38d88e"
"Color palette: https://lospec.com/palette-list/deep-maze"

KEY_UP = "Up"
KEY_LEFT = "Left"
KEY_DOWN = "Down"
KEY_RIGHT = "Right"

def main():

    screen = Screen()
    screen.setup(SCREEN_WIDTH,SCREEN_HEIGHT)
    screen.bgcolor(BACKGROUND_COLOR)
    screen.title("Snake Game!")

    screen.tracer(0)
    screen.listen()

    newSnake = Snake(SNAKE_COLOR)
    newFruit = Fruit(SCREEN_WIDTH, SCREEN_HEIGHT, FRUIT_COLOR)
    newDisplay = Display(TOP_LIMIT,BOTTOM_LIMIT, LEFT_LIMIT, RIGHT_LIMIT, DISPLAY_COLOR)

    screen.onkeypress(newSnake.UpSnake, KEY_UP)
    screen.onkeypress(newSnake.LeftSnake, KEY_LEFT)
    screen.onkeypress(newSnake.DownSnake, KEY_DOWN)
    screen.onkeypress(newSnake.RightSnake, KEY_RIGHT)

    def StartGame():       
        while True:
            screen.update()    
            time.sleep(0.1)

            newSnake.MoveSnake()

            if newSnake.snakeHead.distance(newFruit) < 15:
                newFruit.GenPosition()
                newSnake.AddBodyElement()
                newDisplay.IncreaseScore()

            if  TOP_LIMIT < newSnake.snakeHead.ycor() \
                or LEFT_LIMIT > newSnake.snakeHead.xcor() \
                or BOTTOM_LIMIT > newSnake.snakeHead.ycor()  \
                or RIGHT_LIMIT < newSnake.snakeHead.xcor():
                    time.sleep(0.5)
                    newSnake.RemoveSnake()
                    newFruit.RemoveFruit()
                    newDisplay.SetGameOverText()
                    time.sleep(2.5)
                    newSnake.RestartSnake()                
                    newFruit.SetNewFruit()
                    newDisplay.ResetScore()

            for element in newSnake.snakeBody[1:]:
                if newSnake.snakeHead.distance(element) < 10:
                    time.sleep(0.5)
                    newSnake.RemoveSnake()
                    newFruit.RemoveFruit()
                    newDisplay.SetGameOverText()
                    time.sleep(2.5)
                    newSnake.RestartSnake()
                    newFruit.SetNewFruit()
                    newDisplay.ResetScore()

    try:
        StartGame()
        screen.mainloop()
    except Exception:
        pass

if __name__ == "__main__":
    main()