from tkinter import *

# Colors
lightred = '#ffa0a0'
lightblue = '#7cfcff'
lightgreen = '#c5ffa0'
lightpink = '#ffc5dc'
lightpurple = '#e5c7ff'


class CircleBeat:
    def __init__(self, master):
        self.master = master
        self.gb = None
        self.colors = [lightred, lightblue, lightgreen, lightpink, lightpurple]
        self.width = None
        self.height = None
        self.winc = 0.08
        self.hinc = 0.23
        self.centers = []

    def createCanvas(self, width: int, height: int):
        self.width = width
        self.height = height
        self.gb = Canvas(master=self.master, width=self.width, height=self.height, bg='gray', cursor='dot')
        self.gb.pack()
        self.gb.bind('<Button-1>', self.onClick)

    def draw(self):
        if self.width is None or self.height is None:
            print("Width and height not set.\n")
        else:
            while self.winc + 0.176 < 1 and self.hinc + 0.126 < 1:
                icolors = self.colors
                cnext = icolors.pop(0)
                icolors.append(cnext)
                self.gb.create_oval(self.width * self.winc,
                                    self.height * self.hinc,
                                    self.width * (self.winc + 0.126),
                                    self.height * (self.hinc + 0.126),
                                    activefill='white',
                                    fill=cnext)
                self.winc += 0.178
                if self.winc + 0.178 >= 1:
                    cnext = icolors.pop(0)
                    icolors.append(cnext)
                    self.hinc += 0.156
                    self.winc = 0.08

    def onClick(self, event):
        print('You clicked on {} and {}'.format(event.x, event.y))



    def update(self):
        pass