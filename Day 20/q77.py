r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter columns for Matrix A: "))
r2 = int(input("Enter rows for Matrix B: "))
c2 = int(input("Enter columns for Matrix B: "))

if c1 != r2:
    print("Matrix multiplication is not possible with these dimensions.")
else:
    print("Enter elements for Matrix A:")
    matrix_a = []
    for i in range(r1):
        row = []
        for j in range(c1):
            row.append(int(input(f"A[{i}][{j}]: ")))
        matrix_a.append(row)

    print("Enter elements for Matrix B:")
    matrix_b = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input(f"B[{i}][{j}]: ")))
        matrix_b.append(row)

    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
            cell_sum = 0
            for k in range(c1):
                cell_sum += matrix_a[i][k] * matrix_b[k][j]
            row.append(cell_sum)
        result.append(row)

    print("Resulting Matrix after Multiplication:")
    for row in result:
        print(row)