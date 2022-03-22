import sys

import numpy
import pylab

if __name__ == "__main__":
    xInput, yInput = [], []  # Массивы для исходных точек

    nameFile = "Parabola"
    file = open(nameFile)  # Записываем в массивы исходные координаты x и y
    for lineFile in file.readlines():
        bufFile = list(map(float, lineFile.split()))
        xInput.append(bufFile[0])
        yInput.append(bufFile[1])
    file.close()

    # smoothDegree = int(input()) #Степень полинома
    global smoothDegree
    print("Введите степень полинома")
    smoothDegree = int(input())
    global k  # Степень сглаживания
    print("Введите количество точек для сглаживания")
    k = int(input())

    if smoothDegree > k:
        print("Степень полинома должна быть меньше количества точек для сглаживания")
        sys.exit()
    elif k % 2 == 1:
        print("Количество точек для сглаживания должно быть чётным числом")
        sys.exit()


    def buldd_mat(x, y, iter):
        matFunction = numpy.zeros((len(y), smoothDegree + 1))  # Создаём нулевую матрицу кол-во точек * степень полинома
        seachFactor = [0] * len(y)
        for i in range(len(matFunction)):
            for j in range(len(matFunction[0])):
                matFunction[i][j] = x[i] ** j  # Значения в степени номера столбца

        matFunction = numpy.matrix(matFunction)  # Переводим в объект типа matrix для работы с его методами
        y = numpy.matrix(y)
        y.shape = (len(seachFactor), 1)

        matAllFactor = matFunction.transpose() * matFunction
        masAllFactor = matFunction.transpose() * y

        seachFactor = pylab.linalg.solve(matAllFactor,
                                         masAllFactor)  # Находим коэффициенты полинома решением итоговой системы
        seachFactor = numpy.matrix(seachFactor)
        seachFactor.ravel()
        seachFactor = list(map(float, seachFactor))
        return calculationPolinom(seachFactor, iter)


    def calculationPolinom(polinomFactor, x):  # Вычисления значения полинома в точке x
        sumPolinom = 0
        for i in range(smoothDegree + 1):
            sumPolinom += polinomFactor[i] * (x ** i)
        return sumPolinom


    xFinish, yFinish = [], []  # Создаём массивы для итоговых x и y
    xFinish = xInput

    for i in range(k // 2, len(xInput) - k // 2):
        yFinish.append(buldd_mat(xInput[i - k // 2:i + k // 2 + 1], yInput[i - k // 2:i + k // 2 + 1], xInput[i]))

    pylab.title(nameFile)
    pylab.plot(xInput, yInput, label="исходный график")  # График исходный
    xFinish = xFinish[k // 2:-k // 2]
    line, = pylab.plot(xFinish, yFinish, "mD--", label="Сглаженный график")  # График готовый сглаженный
    line.set_color('red')
    line.set_linewidth(3)
    pylab.legend()

    pylab.show()

    f = open("Output", "w")  # Вывод в файл
    for i in range(len(yFinish)):
        f.write(str(xFinish[i]))
        f.write(" ")
        f.write(str(yFinish[i]))
        f.write("\n")
    f.close()

    """
    pylab.show()
    
    def calculationPolinom(seachFactor, x, smoothDegree, k, j):    #Вычисления значения полинома в точке x
        sumPolinom = 0
    
        for i in range(k + 1):
            sumPolinom += seachFactor[i] *
    
        for i in range(smoothDegree + 1):
            sumPolinom += seachFactor[i] * (x ** i)
        return sumPolinom
    """

    """ Старое тело
    xFinish, yFinish = [], []    #Создаём массивы для итоговых x и y
    deltX = (xInput[-1] - xInput[0]) / 1000
    xCurrent = xInput[0] - deltX
    for i in range(0, 1000):
        xCurrent += deltX
        xFinish.append(xCurrent)
        yFinish.append(calculationPolinom(seachFactor, xCurrent, smoothDegree))
    """

    """
    k = 4
    
    xFinish, yFinish = [], []    #Создаём массивы для итоговых x и y
    for i in range(k // 2, len(xInput) - k // 2):
        yFinish = calculationPolinom(seachFactor, xInput[i], smoothDegree, k, i)
    """

    """
    def smoothLocalData(y, k):    #Сглаживание локальных данных
        y_fin = [0] * len(y)
        for i in range(k // 2, (len(y) - (k // 2))):
            sum = 0
            for j in range(i - k // 2, i + k):
                sum += y[j]
            y_fin[i] = sum / (k + 1)
        return y_fin
    """
