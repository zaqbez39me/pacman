class Road:
    step = 22

    def __init__(self, first_crossroad, second_crossroad):
        self.lx = first_crossroad.x
        self.ly = first_crossroad.y
        self.rx = second_crossroad.x
        self.ry = second_crossroad.y
        if self.lx > self.rx:
            self.lx, self.rx = self.rx, self.lx
        if self.ly > self.ry:
            self.ly, self.ry = self.ry, self.ly

    def len_x(self):
        return self.rx - self.lx

    def len_y(self):
        return self.ry - self.ly
