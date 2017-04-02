from tkinter import *
from colors import *

class CircleBeat:
    def __init__(self):
        self.master = Tk()
        self.master.title('CircleBeat')
        self.master.configure(bg='gray')
        self.master.resizable(width=False, height=False)

        self.topFrame = None
        self.boardFrame = None

        self.gb = None
        self.width = None
        self.height = None
        self.winc = 0.08
        self.hinc = 0.05

        self.colors = Colors().getColors()
        self.centers = []

    def createFrames(self):
        # Creates two frames to divide the top from the board containing circles
        self.topFrame = Frame(master=self.master, bg='red')
        # topFrame = Frame(master=self.master, bg='red', bd=10, relief='sunken')
        #topFrame.grid(row=0, column=0, padx=5, pady=5)
        self.topFrame.grid(row=0, column=0)

        self.boardFrame = Frame(master=self.master, bg='blue')
        self.boardFrame.grid(row=1, column=0, padx=5, pady=5)


        testLabel = Label(master=self.topFrame, text="This is a test")
        testLabel.grid(row=0, column=0, pady=20, sticky=W + S)
        testLabel.configure(bg='purple')

    def createCanvas(self):
        # Creates a canvas of size width x height and disables resizing of the window
        self.gb = Canvas(master=self.boardFrame, width=self.width, height=self.height, bg='gray', cursor='dot')
        self.gb.pack()
        #self.gb.bind('<Button-1>', self.onClick)

    def createCircles(self):
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



    def initialize(self, width: int, height: int):
        # Initiates the creation of the canvas and frames
        # and draws the circles
        try:
            self.width = width
            self.height = height

            if self.width is None or self.width <= 0:
                raise WidthError
            if self.height is None or self.height <= 0:
                raise HeightError


            self.createFrames()
            self.createCanvas()
            self.createCircles()

        except (WidthError, HeightError) as e:
            print('Invalid {}'.format('Width' if e == WidthError else 'Height'))
            exit(0)

    def start(self):
        self.master.mainloop()

    def onClick(self, event):
        print('You clicked on {} and {}'.format(event.x, event.y))

    def update(self):
        pass


class WidthError(Exception):
    pass

class HeightError(Exception):
    pass