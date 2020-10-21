class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __repr__(self):
        return str(self.re) + "+" + str(self.im)

    def __add__ (self, other):
        re = self.re + other.re
        im = self.im + other.im

        return ComplexNumber(re, im)


