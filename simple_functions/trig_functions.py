from simple_functions.functions1 import factorial
from functools import lru_cache

__all__ = ['sin']


def sin(x, terms=100):
    return rsum(x, terms)


@lru_cache(maxsize=None)
def rsum(x, n):
    term = (-1)**n / factorial(2*n+1) * x**(2*n+1)
    return term + rsum(x, n-1) if n else term
