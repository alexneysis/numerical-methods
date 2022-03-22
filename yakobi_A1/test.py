import copy

import math

if __name__ == "__main__":
    print("Здравствуйте!")
    e = 1e-30
    f = open("Input_1")
    b = list(map(int, f.readline().split()))
    a = []
    for st in f.readlines():
        a.append(list(map(int, st.split())))
    f.close()


    def Diag(a):
        flag = True
        for i in range(len(a)):
            sum = 0
            for j in range(len(a[0])):
                if i != j:
                    sum += math.fabs(a[i][j])
            if math.fabs(a[i][i]) >= sum:
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


    k = 0
    x = [0] * len(a)
    y = copy.deepcopy(x)  # Создаем временный массив для каждой итерации
    buf = math.inf

    while Check_Error(x, y) < buf:  # Пока уменьшается разность между корнми считаем
        k += 1
        for i in range(len(x)):
            sum = 0
            for j in range(len(x)):
                if i != j:
                    sum += x[j] * a[i][j]
                    if math.fabs(a[i][i]) != e:
                        x[i] = (b[i] - sum) / a[i][i]
                    else:
                        print("Деление на нулевой элемент.")
                        break
        buf = Check_Error(x, y)
        if buf < e:  # Проверка вычисления, если точность устраивает прекращаем дальнейшую работу
            break
        else:
            y = copy.deepcopy(x)  # Сохраняем результат нахождения корней

    if Diag(a):
        print("Ответ = ", x)
    else:
        print("Ответ = ", x, ", но он может быть не точный т.к. нет диагонального преобладания")

    print("Спасибо!")
