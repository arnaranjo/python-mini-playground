'''
ISS current location web:
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/
IMG source:
    https://en.wikipedia.org/wiki/Equirectangular_projection
'''

import requests
import tkinter as tk
from PIL import Image
from turtle import RawTurtle, TurtleScreen

API_URL = "http://api.open-notify.org/iss-now.json"
BACKGROUND_IMG = "ISSTraker/worldmap.png"
WIDTH :int
HEIGHT :int

def DetermineImgSize():
    global WIDTH
    global HEIGHT

    imgSize = Image.open(BACKGROUND_IMG)

    WIDTH, HEIGHT = imgSize.size

def RequestLocation():

    reqLocation = requests.get(API_URL)
    reqData = reqLocation.json()

    lon = float(reqData["iss_position"]["longitude"])
    lat = float(reqData["iss_position"]["latitude"])

    return (lon, lat)

def main():
    
    newWindow = tk.Tk()
    newWindow.config(width = WIDTH, height = HEIGHT)
    newWindow.title("ISS Traker")

    newCanvas = tk.Canvas(newWindow, width = WIDTH, height = HEIGHT)
    newCanvas.pack()

    screen = TurtleScreen(newCanvas, "circle")
    screen.setworldcoordinates(
        llx = -180.0,
        lly = -90.0,
        urx = 180.0,
        ury = 90.0
    )

    issTurtle = RawTurtle(screen)

    backgronundIMG = tk.PhotoImage(file = BACKGROUND_IMG)
    newCanvas.create_image((0,0), image = backgronundIMG)

    
    issTurtle.goto(RequestLocation())

    newWindow.mainloop()

if __name__ == "__main__":
    DetermineImgSize()
    main()
    RequestLocation()