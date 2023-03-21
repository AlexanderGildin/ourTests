class TTime:
    def __init__(self, a, b=None):
        if not b:
            tmp = a.split(':')
            self.h = tmp[0]
            self.m = tmp[1]
        else:
            self.h = str(a)
            self.m = str(b)

    def __repr__(self):
        return self.h.rjust(2, '0') + ':' + self.m.rjust(2, '0')
