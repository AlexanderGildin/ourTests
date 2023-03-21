class TimeException(Exception):
    pass


class TTime:
    def __init__(self, a, b=None):
        if b is None:
            self.h, self.m = map(int, a.split(':'))
        else:
            self.h, self.m = a, b

    def __repr__(self):
        return f'{0 if self.h < 10 else ""}{self.h}:{0 if self.m < 10 else ""}{self.m}'

    def __add__(self, other):
        if type(other) == int:
            self.m += other
            if self.m >= 60:
                self.h += 1
                self.m %= 60
                self.h %= 24
            return TTime(self.h, self.m)
        elif type(other) == TTime:
            self.m += other.m
            self.h += other.h
            if self.m >= 60:
                self.h += 1
                self.m %= 60
            if self.h >= 24:
                self.h %= 24
            return TTime(self.h, self.m)
        else:
            raise TimeException

    def __iadd__(self, other):
        if type(other) == int:
            self.m += other
            if self.m >= 60:
                self.h += 1
                self.m %= 60
                self.h %= 24
            return TTime(self.h, self.m)
        elif type(other) == TTime:
            self.m += other.m
            self.h += other.h
            if self.m >= 60:
                self.h += 1
                self.m %= 60
            if self.h >= 24:
                self.h %= 24
            return TTime(self.h, self.m)
        else:
            raise TimeException

    def __sub__(self, other):
        if type(other) == int:
            self.m -= other
            if self.m >= 60:
                self.h -= 1
                self.m %= 60
                self.h %= 24
            return TTime(self.h, self.m)
        elif type(other) == TTime:
            self.m -= other.m
            self.h -= other.h
            if self.m >= 60:
                self.h -= 1
                self.m %= 60
            if self.h >= 24:
                self.h %= 24
            return TTime(self.h, self.m)
        else:
            raise TimeException

    def __isub__(self, other):
        if type(other) == int:
            self.m -= other
            if self.m >= 60:
                self.h -= 1
                self.m %= 60
                self.h %= 24
            return TTime(self.h, self.m)
        elif type(other) == TTime:
            self.m -= other.m
            self.h -= other.h
            if self.m >= 60:
                self.h -= 1
                self.m %= 60
            if self.h >= 24:
                self.h %= 24
            return TTime(self.h, self.m)
        else:
            raise TimeException
