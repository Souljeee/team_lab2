import numpy as np

def main():
    try:
        n = int(input("Введите количество строк (N): "))
        m = int(input("Введите количество столбцов (M): "))

        if n <= 0 or m <= 0:
            print("Размерности матрицы должны быть положительными числами.")
            return

        if n != m:
            print("Матрица должна быть квадратной (N должно равняться M) для вычисления определителя.")
            return

        matrix = []
        print("Введите элементы матрицы:")

        for i in range(n):
            row = []
            for j in range(m):
                element = float(input(f"Элемент ({i+1},{j+1}): "))
                row.append(element)
            matrix.append(row)

        determinant = np.linalg.det(matrix)

        print("Матрица:")
        for row in matrix:
            print(row)

        print("Определитель матрицы:", determinant)

    except ValueError:
        print("Пожалуйста, введите корректные числа.")
    except np.linalg.LinAlgError:
        print("Матрица вырожденная, определитель не может быть вычислен.")

if __name__ == "__main__":
    main()
