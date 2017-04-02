class Colors:
    """ A class containing all the colors that may be used for the circles
    """
    def __init__(self):
        self.red = '#ffa0a0'
        self.blue = '#7cfcff'
        self.green = '#c5ffa0'
        self.pink = '#ffc5dc'
        self.purple = '#e5c7ff'

    def getColors(self):
        """ Returns a list of all the colors in hex form"""
        return [self.red, self.blue, self.green, self.pink, self.purple]
