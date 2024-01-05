def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, bottom):

        if type(top) != int or type(bottom) != int:
            raise RuntimeError("Numerator and Denominator must be integer values")

        self.num = top
        self.den = bottom
        if self.den < 0:
            self.den = self.den*-1
            self.num = self.num*-1
        common = gcd(self.num, self.den)
        self.num = self.num//common
        self.den = self.den//common

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def show(self):
        print(self.num, "/", self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        return Fraction(newnum, newden)

    def __gt__(self, other):
        return self.num/self.den > other.num/other.den

    def __ge__(self, other):
        return self.num / self.den >= other.num / other.den

    def __lt__(self, other):
        return self.num / self.den < other.num / other.den

    def __le__(self, other):
        return self.num / self.den <= other.num / other.den

    def __ne__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __radd__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        return Fraction(newnum, newden)

    def __iadd__(self, other):
        self.num = self.num * other.den + self.den * other.num
        self.den = self.den * other.den
        return Fraction(self.num, self.den)

    def __repr__(self):
        return str(self.num) + "/" + str(self.den)
