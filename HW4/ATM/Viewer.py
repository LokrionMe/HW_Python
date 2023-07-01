class Viewer(object):
    def __init__(self, obj):
        self.x = obj
        print(self.x)
    def __add__(self, other):
        return Viewer(self.x + other.x)