class TTime:
    def __init__(self, a, b=None):
        if not b:
            tmp = a.split(':')
            self.h = int(tmp[0])
            self.m = int(tmp[1])
        else:
            self.h = a
            self.m = b

    def __repr__(self):
        h = str(self.h)
        m = str(self.m)
        return h.rjust(2, '0') + ':' + m.rjust(2, '0')
