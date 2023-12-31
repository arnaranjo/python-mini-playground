'''
ISS current location web:
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/
Icon:
    https://www.flaticon.com/free-icon/space-station_3212670
'''

from iss import issTrakerTurtle
import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image

API_URL = "http://api.open-notify.org/iss-now.json"
BACKGROUND_IMG = "ISSTraker/worldmap.png"
WIDTH :int
HEIGHT :int
UPDATE_TIME = 5000
FONT_FAMILY = "arial"
FONT_SIZE = 11
FONT_TYPE = "normal"

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

def Exit():
    quit()

def About():
    messagebox.showinfo(
        title = "About",
        message = 
'''Where is the ISS?\n
Don't worry, NASA has lost our space ship more than we expected but thanks to this app We can now stay updated on its location easily!\n
https://github.com/arnaranjo/python-mini-playground'''
    )

def main():
    DetermineImgSize()

    newWindow = tk.Tk()
    newWindow.title("ISS Traker")
    newWindow.resizable(False,False)
    menuBar = tk.Menu()

    newWindow.config(
        width = WIDTH,
        height = HEIGHT,
        menu = menuBar,
        padx = 20,
        pady = 20
    )

    menuView = tk.Menu(menuBar, tearoff = "off")
    menuBar.add_cascade(labe = "View", menu = menuView)
    menuHelp = tk.Menu(menuBar, tearoff = "off")
    menuBar.add_cascade(label = "Help", menu = menuHelp)

    newCanvas = tk.Canvas(width = WIDTH,height = HEIGHT)
    newCanvas.pack()

    newISS = issTrakerTurtle(newCanvas, RequestLocation())

    backgronundIMG = tk.PhotoImage(file = BACKGROUND_IMG)
    newCanvas.create_image((0,0), image = backgronundIMG)

    newISS.setISS()

    menuView.add_command(
        label = "Update ISS location",
        command = lambda: newISS.UpdateISSLocation(RequestLocation()),
        font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)
    )
    menuView.add_command(
        label = "Exit",
        command = Exit,
        font = (FONT_FAMILY, FONT_SIZE, FONT_TYPE)
    )
    menuHelp.add_command(
        label = "About...",
        command = About
    )

    def UpdateLocation():
        newISS.UpdateISSLocation(RequestLocation())

        newWindow.after(
            ms = UPDATE_TIME,
            func = UpdateLocation
        )  

    newWindow.mainloop() 

if __name__ == "__main__":
    main()