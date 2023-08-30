import tkinter as tk

BACKGROUND = "ISSTraker/worldmap.png"

newWindow = tk.Tk()

backgronundIMG = tk.PhotoImage(file = BACKGROUND)
newCanvas = tk.Canvas(width = 1430,height = 735)
newCanvas.pack()
newCanvas.create_image((715.0,367.5), image = backgronundIMG)


newWindow.mainloop()