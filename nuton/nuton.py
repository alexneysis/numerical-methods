import math

import numpy
import pylab

if __name__ == "__main__":
    f = open("Log")  # Чтенеи из файла первый столбец x второй y
    x = []
    y = []
    for strs in f.readlines():
        buf = list(map(float, strs.split()))
        x.append(buf[0])
        y.append(buf[1])
    f.close()

    global kolDot  # Количество точек изначальное
    kolDot = len(x)

    global h  # Находим между точками по условию == const
    h = x[1] - x[0]

    deltY = numpy.zeros((kolDot - 1, kolDot))  # Матрица разностей
    for j in range(kolDot - 1):
        deltY[0][j] = y[j + 1] - y[j]
    for k in range(1, kolDot):
        for j in range(kolDot - (k + 1)):
            deltY[k][j] = deltY[k - 1][j + 1] - deltY[k - 1][j]

    resY = numpy.zeros((kolDot, kolDot))  # Матрица для y и их разниц (для удобства работы алгоритма)
    resY[0] = y  # Добавляем массив y
    for i in range(kolDot - 1):  # Добавляем матрицу разностей y
        resY[i + 1] = deltY[i]


    def fT(t):
        masT = [0] * kolDot
        masT[0] = 1
        masT[1] = t
        for i in range(2, kolDot):
            masT[i] = masT[i - 1] * (t + i - 1)
        return masT


    def f(t):
        masT = fT(t)
        sumD = 0
        for i in range(kolDot):
            for j in range(kolDot):
                if j == (kolDot - 1) - i:
                    sumD += (resY[i][j] * masT[i]) / math.factorial(i)
        return sumD


    deltX = (x[-1] - x[0]) / (1000 - 1)  # Шаг изменения x
    x0 = x[0] - deltX

    masResYF = []
    masResXF = []
    for i in range(1000):  # Основной цикл для расчета Y и X функции
        x0 += deltX
        masResXF.append(x0)
        t = (x0 - x[-1]) / h
        masResYF.append(f(t))

    pylab.plot(x, y)
    line, = pylab.plot(x, y)
    line.set_color('red')
    line.set_linewidth(3)

    line, = pylab.plot(masResXF, masResYF)
    line.set_color('blue')
    line.set_linewidth(1)
    pylab.show()

    f = open("Output", "w")  # Вывод в файл
    for i in range(len(masResXF)):
        f.write(str(masResXF[i]))
        f.write(" ")
        f.write(str(masResYF[i]))
        f.write("\n")
    f.close()
