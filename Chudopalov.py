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
        try:
            if type(other) == int:
                if other <= 60:
                    return TTime(self.a, self.b + other)
                else:
                    self.a += 1
                    return TTime(self.a, self.b + other)
            else:
                if self.b <= 60 or other.b <= 60:
                    return TTime(self.a + other.a, self.b + other.b)
                else:
                    self.a += 1
                    return TTime(self.a + other.a, self.b + other.b)
        except TimeException:
            pass

    def __iadd__(self, other):
        try:
            if type(other) == int:
                if self.b <= 60 or other.b <= 60:
                    self.a += other.a
                    self.b += other.b
                    return TTime(self.a, self.b)
            else:
                self.a += 1
                self.a += other.a
                self.b += other.b
                return TTime(self.a, self.b)
        except TimeException:
            pass

    def __sub__(self, other):
        try:
            if self.b <= 60 or other.b <= 60:
                return TTime(self.a - other.a, self.b - other.b)
            else:
                self.a += 1
                return TTime(self.a - other.a, self.b - other.b)
        except TimeException:
            pass

    def __isub__(self, other):
        try:
            if self.b <= 60 or other.b <= 60:
                self.a -= other.a
                self.b -= other.b
                return TTime(self.a, self.b)
            else:
                self.a += 1
                self.a -= other.a
                self.b -= other.b
                return TTime(self.a, self.b)
        except TimeException:
            pass


# перезагрузить метод __add__
# если прибавляется число, то к текущему времени нужно прибавить это количество минут, если прибавляется обьект типа TTime,
# то прибавляется это количество часов и это количество минут
# __iadd__
# __sub__
