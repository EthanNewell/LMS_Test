from PIL import Image as im
from PIL import ImageDraw as draw
 
 
class Drawer:
    def __init__(self, draw_map, cell_size, color="black"):
        self.draw_map = draw_map
        self.cell_size = cell_size
        self.num_to_color = {i: color for i in self.numbers()}
 
    def numbers(self):
        ret = []
        for i in self.draw_map:
            ret += i
        return list(sorted(list(set(ret))))
 
    def set_color(self, number, color):
        self.num_to_color[number] = color
 
    def set_cell_size(self, cell_size):
        self.cell_size = cell_size
 
    def size(self, mult=True):
        if mult:
            return len(self.draw_map[0]) * self.cell_size, \
                   len(self.draw_map) * self.cell_size
        return len(self.draw_map[0]), len(self.draw_map)
 
    def draw(self):
        image = im.new("RGB", (self.size()[0], self.size()[1]), (0, 0, 0))
        desk = draw.Draw(image)
        size = self.size(mult=False)
 
        for i in range(size[1]):
            for j in range(size[0]):
                desk.rectangle((self.cell_size * j, self.cell_size * i,
                                self.cell_size * (j + 1) - 1, self.cell_size * (i + 1) - 1),
                               fill=self.num_to_color[self.draw_map[i][j]])
 
        return image
