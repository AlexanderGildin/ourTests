class TTime:
    def __init__(self, h, m=None):
        if not m:
            h = h.split(':')
            self.h = h[0]
            self.m = h[1]
        else:
            self.h = h
            self.m = m

    def __repr__(self):
        return f'{self.h.rjust(2, "0")}:{self.m.rjust(2, "0")}'
