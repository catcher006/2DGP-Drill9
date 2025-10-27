from pico2d import load_image


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x = 400
        self.y1 = 6
        self.y2 = 30
        self.time = 0

    def draw(self):
        if self.time % 2 == 0:
            self.image.draw(self.x, self.y1)
        else:
            self.image.draw(self.x, self.y2)
        self.time += 1

    def update(self):
        pass