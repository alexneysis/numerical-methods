import math

import pylab

if __name__ == "__main__":
    masY, masX = [], []
    x = -7
    deltX = 2 / 3
    for i in range(20):
        x += deltX
        masX.append(x)
        masY.append(x * x + pylab.random() * 6)

    pylab.plot(masX, masY)

    pylab.show()

    for i in range(len(masX)):
        print(masX[i], " ", masY[i])
