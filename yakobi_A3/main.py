from sympy import symbols
from sympy.parsing.mathematica import mathematica

if __name__ == "__main__":
    x, y = symbols("x, y")
    fun = mathematica("sin[x]+1+cos[x]*tan[y*y]")
    print(fun)
