'''
ISS current location web:
    http://open-notify.org/Open-Notify-API/ISS-Location-Now/
'''

from gui import issTrakerTurtle
import tkinter as tk
import requests
from PIL import Image

API_URL = "http://api.open-notify.org/iss-now.json"
BACKGROUND_IMG = "ISSTraker/worldmap.png"
WIDTH :int
HEIGHT :int
UPDATE_TIME = 5.0

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
    newWindow.title("ISS Traker")
    newWindow.config(width = WIDTH,height = HEIGHT)
        
    newCanvas = tk.Canvas(width = WIDTH,height = HEIGHT)
    newCanvas.pack()

    newISS = issTrakerTurtle(newCanvas, RequestLocation())

    backgronundIMG = tk.PhotoImage(file = BACKGROUND_IMG)
    newCanvas.create_image((0,0), image = backgronundIMG)

    newISS.setISS()
    
    newWindow.mainloop() 

if __name__ == "__main__":

    DetermineImgSize()
    main()