# -*- coding: utf-8 -*-
"""
The HFSS expression generator.

"""
from __future__ import division, print_function, unicode_literals, absolute_import

import warnings
warnings.simplefilter('default')


class Expression(object):
    """
    An HFSS expression.

    This object enables manipulation of HFSS expressions using Python
    arithmetic operators, which is much more convenient than manipulating
    their string representation.

    Parameters
    ----------
    expr : str
        Initialize the expression using its string representation.

    Attributes
    ----------
    _raw_string : str
        The string representation of the expression object.

    Raises
    ------
    NotImplementedError
        For operations involving floor division (Python 2 '/' or
        Python 3 '//')

    """
    def __init__(self, expr):
        self.expr = str(expr)

    def __str__(self):
        return self.expr

    def __repr__(self):
        return self.expr

    def __abs__(self):
        """Overloads abs() function."""
        return Expression('abs({0})'.format(str(self)))

    def __add__(self, y):
        """Overloads the addition (+) operator."""
        return Expression('({0}) + ({1})'.format(str(self), str(y)))

    def __radd__(self, y):
        return Expression('({1}) + ({0})'.format(str(self), str(y)))

    def __sub__(self, y):
        """Overloads the subtraction (-) operator."""
        return Expression('({0}) - ({1})'.format(str(self), str(y)))

    def __rsub__(self, y):
        return Expression('({1}) - ({0})'.format(str(self), str(y)))

    def __mul__(self, y):
        """Overloads the multiplication (*) operator."""
        return Expression('({0}) * ({1})'.format(str(self), str(y)))

    def __rmul__(self, y):
        """Overloads the multiplication (*) operator."""
        return Expression('({1}) * ({0})'.format(str(self), str(y)))

    def __truediv__(self, y):
        """Overloads the Python 3 division (/) operator."""
        return Expression('({0}) / ({1})'.format(str(self), str(y)))

    def __rtruediv__(self, y):
        """Overloads the Python 3 division (/) operator."""
        return Expression('{1} / ({0})'.format(str(self), str(y)))

    def __div__(self, y):
        """Overloads the Python 3 floor division (//) operator."""
        raise NotImplementedError("""Integer division is not implemented by
design.  Please use from __future__ import division in the calling code.""")

    def __rdiv__(self, y):
        """Overloads the Python 3 floor division (//) operator."""
        raise NotImplementedError("""Integer division is not implemented by
design.  Please use from __future__ import division in the calling code.""")

    def __neg__(self):
        """Overloads the negation (-) operator."""
        return Expression('-({0})'.format(str(self)))

    def __pow__(self, y):
        """Overloads the power (**_ operator."""
        return Expression('({0}) ^ ({1})'.format(str(self), str(y)))

    def __rpow__(self, y):
        """Overloads the power (**_ operator."""
        return Expression('({1}) ^ ({0})'.format(str(self), str(y)))

if __name__ == "__main__":
    a = Expression('0.010in')
    b = a + 2
    c = (a + b) / a
    d = a / (a + b)
    e = (a + b) * a
    f = a * (a + b)

    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)