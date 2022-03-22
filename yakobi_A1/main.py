import copy
import math

if __name__ == "__main__":
    f = open("Input_1")
    b = list(map(int, f.readline().split()))
    mat = []
    for str in f.readlines():
        mat.append(list(map(int, str.split())))
    f.close()


    def Check_Diag(mat):  # Проверка диагонального преобладания
        flag = True
        for i in range(len(mat)):
            sum = 0
            for j in range(len(mat[0])):
                if i != j:
                    sum += math.fabs(mat[i][j])
            if math.fabs(mat[i][i]) >= sum:
                continue
            else:
                flag = False
        return flag


    def Check_Error(x, y):  # Поиск максимальнйо разницы между корнями
        max = math.fabs(math.fabs(x[0]) - math.fabs(y[0]))
        for i in range(1, len(x)):
            if math.fabs(math.fabs(x[i]) - math.fabs(y[i])) > max:
                max = math.fabs(math.fabs(x[i]) - math.fabs(y[i]))
        return max


    E = 1e-3  # Точность вычисления
    x = [0] * len(mat)  # Вектор неизвестных
    y = copy.deepcopy(x)  # Создаем временный массив для каждой итерации
    buf = math.inf
    while Check_Error(x, y) < buf:  # Пока уменьшается разность между корнми считаем
        for i in range(len(x)):
            sum = 0
            for j in range(len(x)):  # Считаем сумму коэффициентов * неизвестные
                if i != j:
                    sum += x[j] * mat[i][j]
            if mat[i][i] != 0:
                y[i] = (b[i] - sum) / mat[i][i]
            else:
                print("Найден нулевой элемент в диагональной матрице")
                break
        buf = Check_Error(x, y)
        if buf < E:  # Проверка вычисления, если точность устраивает прекращаем дальнейшую работу
            print("Hello")
            break
        else:
            x = copy.deepcopy(y)  # Сохраняем результат нахождения корней

    if Check_Diag(mat):
        print("Ответ = ", x)
    else:
        print("Ответ = ", x, ", но он может быть не точный т.к. нет диагонального преобладания")

    """
    import numpy
    import copy
    def Transpose(mat):    #Не работает с не квадратными матрицами
        t = numpy.zeros((len(mat[0]), len(mat)))
        for i in range(len(t)):
            for j in range(len(t[0])):
                t[i][j] = mat[j][i]
        return t
    
    
    def PrintMat(mat):    #Красивая печать матрицы
        for i in mat:
            for j in i:
                print(j, end=" ")
            print()
        print()
    
    def Lmat(mat):    #Выборка левой треугольной матрицы
        t = copy.deepcopy(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j < i:
                    continue
                else:
                    t[i][j] = 0
        return t
    
    def Rmat(mat):    #Выборка правой треугольной матрицы
        t = copy.deepcopy(mat)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j > i:
                    continue
                else:
                    t[i][j] = 0
        return t
    
    def Dmat(mat):    #Выборка диагональнных элементов
        t = copy.deepcopy(mat)
    
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if j == i:
                    continue
                else:
                    t[i][j] = 0
        return t
    
    def Dmat_obr(mat):
        t = numpy.eye(len(mat), len(mat[0]), dtype=float)
        flag = True
        for i in range(len(mat)):
            if mat[i][i] != 0:
                t[i][i] = 1/mat[i][i]
            else:
                flag = False
        if flag:
            return t
        else:
            print("В диагонале матрицы содержаться нули")
            return False
    
    def Sum_mat(a, b):
        if (len(a) == len(b)) and (len(a[0]) == len(b[0])):
            c = numpy.zeros((len(a), len(a[0])))
            for i in range(len(a)):
                for j in range(len(a[0])):
                    c[i][j] = a[i][j] + b[i][j]
            return c
        else:
            print("Разные размерности")
    
    def Init_B(mat):
        buf = numpy.dot(-Dmat_obr(mat), Sum_mat(Rmat(mat), Lmat(mat)))
        return buf
    def Init_g(mat, b):
        g = numpy.dot(Dmat_obr(mat), b)
        return g
    mat = [[2, 1, 1],
           [1, -1, 0],
           [3, -1, 2]]
    b = [2, -2, 2]
    
    print("Нижний треугольный")
    for i in Lmat(mat):
        print(i)
    print("Верхний треугольный")
    for i in Rmat(mat):
        print(i)
    print("Диагональ матрицы")
    for i in Dmat(mat):
        print(i)
    print("Транспонированая")
    print(Transpose(mat))
    print("Обратная диагональная")
    print(Dmat_obr(mat))
    print("Марица B")
    for i in Init_B(mat):
        print(i)
    print("Массив g")
    print(Init_g(mat, b))
    """
