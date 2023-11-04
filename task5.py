def find_min_element(matrix):
    min_element = matrix[0][0]
    min_row, min_col = 0, 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] < min_element:
                min_element = matrix[i][j]
                min_row, min_col = i, j

    return min_element, min_row, min_col

def main():
    try:
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))

        if n <= 0 or m <= 0:
            print("Размерности матрицы должны быть положительными числами.")
            return

        matrix = []
        print("Введите элементы матрицы:")

        for i in range(n):
            row = []
            for j in range(m):
                element = float(input(f"Элемент ({i+1},{j+1}): "))
                row.append(element)
            matrix.append(row)

        min_element, min_row, min_col = find_min_element(matrix)

        print("Матрица:")
        for row in matrix:
            print(row)

        print("Минимальный элемент:", min_element)
        print("Индексы минимального элемента: ({}, {})".format(min_row, min_col))

    except ValueError:
        print("Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    main()
