import os
import sys


def main():
    pass

# CMD UI Data Structure 
#   : Text Version of UI is created in UI Object creation.
BLANK       = " "
CORNER      = "+"
HORIZONTAL  = "-"
VERTICAL = "|" 



class Diagram:

    # Data Structure that can include other UI Structures.

    def __init__(self, width, height):
        self.width = width
        self.width = height
        self.text_print = _create_rectangle(width, height, BLANK)

class Rectangle:
    def __init__(self, x, y, width, height, fill, stroke):
        self.x = x
        self.y = y
        self.text_print = _create_rectangle(width, height, 
            BLANK if fill == "white" else "%")

class Text:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]

        

class DiagramFactory:
    def make_diagram(self, width, height):
        return Diagram(width, height)

if __name__=="__main__":
    main()

