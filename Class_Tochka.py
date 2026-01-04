class Dot(object):
    def __init__(self, koordinata_x, koordinata_y):
        self.x = koordinata_x
        self.y = koordinata_y

    def __str__(self):
        return self.x, self.y

    def print(self):
        print(self.__str__())
