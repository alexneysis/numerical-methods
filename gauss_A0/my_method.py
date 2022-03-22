if __name__ == "__main__":
    # Метод Гаусса
    f = open("Input.txt")
    RANGE = int(f.read(1))  # Записываем количество строк матрицы

    COLUMN = int(f.read(1))  # Записываем количество столбцов матрицы

    mat = []  # Считываем матрицу из файла
    f.read(1)
    for line in f.readlines():
        mat.append(line.split())

    for i in range(RANGE):  # Преобразуем матрицу к вещественным числам
        for j in range(COLUMN):
            mat[i][j] = float(mat[i][j])
    f.close()

    mas = []  # Создаем массив для записи искомых переменных (обратный ход)


    def next_run(mainIndex):  # Прямой ход
        i = mainIndex
        while i < RANGE - 1:  # Зануляем все элементы под элементом главной диагонали
            if mat[i + 1][mainIndex] != 0 and mat[mainIndex][mainIndex] != 0:
                kof = mat[i + 1][mainIndex] / mat[mainIndex][
                    mainIndex] * -1  # Находим множитель для дальнейших преобразований
                transf(i, mainIndex, kof)
            i += 1


    def transf(secondIndex, mainIndex, kof):  # Складываем строку побочную с главной строкой умноженной на коэффициент
        j = mainIndex
        while j < COLUMN:
            mat[secondIndex + 1][j] = mat[mainIndex][j] * kof + mat[secondIndex + 1][j]
            j += 1


    def back_run(mainIndex):  # Обратный ход
        j = mainIndex
        sum = 0
        while j + 1 < COLUMN - 1:  # Находим сумму коэффициентов умноженную на найденные переменные
            sum += mat[mainIndex][j + 1] * mas[case_mas(j + 1)]
            j += 1

        sum = (sum * -1 + mat[mainIndex][COLUMN - 1]) / mat[mainIndex][
            mainIndex]  # Находим неизвестное член и добавляем его в массив
        mas.append(sum)


    def case_mas(i):  # Находим индекс элемента для соответствующего коэффициента
        return RANGE - (i + 1)


    print("Добро пожаловать сейчас мы приведем матрицу к "  # Основное тело программы
          "треугольному виду и найдем неизвестные методом Гаусса")

    print("Исходная матрица")
    for i in mat:  # Выводим матрицу
        print(i)
    print()

    for i in range(RANGE - 1):  # Прямой ход
        next_run(i)

    print("Преобразованная матрица")
    for i in mat:  # Выводим матрицу
        print(i)
    print()

    if mat[RANGE - 1][RANGE - 1] == 0:  # Обратный ход
        print("Метод Гаусса не работает")
    else:
        i = RANGE - 1
        while i >= 0:
            back_run(i)
            i -= 1
        print("Искомые переменные\n", mas)  # Выводим искомый массив переменных
