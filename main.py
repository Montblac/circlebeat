from circlebeat import *

if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    gb = CircleBeat(root)
    gb.createCanvas(500, 500)
    gb.draw()
    root.mainloop()
