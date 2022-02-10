import math
class world2screen:
    def __init__ (self):
        self.alpha = 65.7407
    def calc_dist_to_coord (self, dist_x, dist_y):
        w1 = math.cos (self.alpha) * dist_y
        h1 = math.sin (self.alpha) * dist_y
        w2 = math.cos (self.alpha) * dist_x
        h2 = math.sin (self.alpha) * dist_x
        w = ((w1+w2)/2)
        h = ((h1+h2)/2)
        return w,h
        