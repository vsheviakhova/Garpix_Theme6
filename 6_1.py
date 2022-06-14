class Parallelepiped():
    def __init__(self, width, length, height):
        self.width = width
        self.length = length
        self.height = height

    def get_volume(self):
        print(self.width * self.length * self.height)

    def get_square_base(self):
        print(self.width * self.length)

    def get_square_side(self, edge, height):
        print(edge * height)

    @staticmethod
    def info():
        print('Методы, доступные в этом классе:\n'
            'get_volume()\n'
            'get_square_base()\n'
            'get_square_side()\n')


box = Parallelepiped(3, 4, 7)
print(box.width)
print(box.length)
print(box.height)
box.info()
box.get_volume()
box.get_square_base()
box.get_square_side(3, 7)
