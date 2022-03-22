if __name__ == "__main__":

    a = [[1, 2, 3],
         [4, 5, 6],
         [7, 2, 9]]
    t = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
    b = [1, 1, 1]
    n, m = 3, 4
    x = [0, 0, 0]

    for i in range(3):  # Вывод
        for j in range(3):
            print("%-4d" % a[i][j], end=" ")
        print(b[i], end="\n")
    print("\n")

    for k in range(0, n - 1):  # Прямой ход
        for i in range(k + 1, n):
            t[i][k] = a[i][k] / a[k][k]
            b[i] = b[i] - t[i][k] * b[k]
            for j in range(k, n):
                a[i][j] = a[i][j] - t[i][k] * a[k][j]

    x[n - 1] = b[n - 1] / a[n - 1][n - 1]  # Обратный ход
    for k in range(n - 2, 0 - 1, -1):
        sum = 0
        for j in range(k + 1, n):
            sum += a[k][j] * x[j]
        x[k] = (b[k] - sum) / a[k][k]

    for i in range(3):  # Вывод
        for j in range(3):
            print("%-4d" % a[i][j], end=" ")
        print(b[i], end="\n")

    print("\n", x)
