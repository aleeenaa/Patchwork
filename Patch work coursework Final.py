#-------------------------------------------------------------------------------
# Python Coursework: A Patchwork Sampler
# Aleena Naeem
# 716038
# Autumn Teaching Block 2013
#-------------------------------------------------------------------------------

from graphics import *
colour = ["","",""]

def main():
    size= getSize()
    colour = getColour()
    win = GraphWin("Patchwork", size*100, size*100)
    drawPatches(win, size)
# Python Patchwork Coursework
# Aleena Naeem
# 716038

def getSize():
    while True:
        size = ""
        while not(size.isdecimal()):
            size = input("Please enter a valid size between 2 - 9 for your patchwork:")
            if not(size.isdecimal()):
                print("Only digits are allowed.")
        size = eval(size)
        if size < 2 or size > 9:
            print("The valid numbers are 2 - 9.")
        else:
            return size

def getColour():
    for i in range(3):
        chosenColour = validateColour(i + 1)
        colour[i] = chosenColour
    return colour

def validateColour(colourNumber):
        while True:
            colour1 = input("Please pick 3 colours {0}:".format(colourNumber))
            if (colour1 == "red" or colour1 == "blue" or colour1 == "green" or
            colour1 == "cyan" or colour1 == "magenta"):
                if repetitiveColour(colour1):
                    return colour1
                else:
                    print("Cannot enter the same colour more than once.")
            else:
                print("The possible colours are; red, blue, green, cyan and magenta.")

def repetitiveColour(colour1):
    return(colour1 != colour[0] and colour1 != colour[1] and colour1 != colour[2])

def selectingColour(row, size, column):
    return(column * size + row)%3

def drawLine(win, p1, p2, colour):
    line = Line(p1, p2)
    line.setOutline(colour)
    line.draw(win)

def drawRectangle(win, p1, p2, colour):
    square = Rectangle(p1, p2)
    square.setFill(colour)
    square.draw(win)

def drawPatchOne(win, position, colour):
    x = position.getX()
    y = position.getY()
    for i in range(5):
        drawLine(win, Point(x + 20*i, y),
        Point(x + 100, y + 100 - 20*i), colour)
        drawLine(win, Point(x, y + 20*i),
        Point(x + 100 - 20*i , y + 100), colour)
        drawLine(win, Point(x + 100 - 20*i, y),
        Point(x, y + 100 - 20*i), colour)
        drawLine(win, Point(x + 20*i, y + 100),
        Point(x + 100, y + 20*i), colour)

def drawPatchTwo(win, position, colour):
    x = position.getX()
    y = position.getY()
    drawRectangle(win, Point(x + 0, y + 0), Point(x + 100, y + 100), colour)
    for i in range(5):
        drawRectangle(win, Point(x + 5 + 20*i, y + 0),
         Point(x + 15 + 20*i, y + 90), "white")
    for i in range(5):
        for j in range(5):
            drawRectangle(win, Point(x + j*20, y + 10 + i*20),
             Point(x + (j+1)*20, y + (i+1)*20), "white")

def drawPatches(win, size):
    for row in range(size):
        for column in range(size):
            if (row % 2 == 0 and column % 2 != 0 or
            row % 2 != 0 and column % 2 == 0):
                drawPatchTwo(win, Point(row*100, column*100),
                colour[selectingColour(row, size, column)])
            else:
                drawPatchOne(win, Point(row*100, column*100),
                colour[selectingColour(row, size, column)])