from math import gcd

class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)
    
    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)
    
    def __add__(self, other):
        n = self.numer * other.denom + self.denom * other.nomer
        d = self.denom * other.denom
        g = gcd(n, d)
        return Ratio(n // g, d // g)