def get_matrix_sum(matrix):
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0
    n = len(matrix)
    m = len(matrix[0])

    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][m - 1 - i]

    return main_diagonal_sum, secondary_diagonal_sum

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

        main_diagonal_sum, secondary_diagonal_sum = get_matrix_sum(matrix)

        print("Матрица:")
        for row in matrix:
            print(row)

        print("Сумма элементов на главной диагонали:", main_diagonal_sum)
        print("Сумма элементов на побочной диагонали:", secondary_diagonal_sum)

    except ValueError:
        print("Пожалуйста, введите корректные числа.")

if __name__ == "__main__":
    main()
