rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for Matrix A:")
matrix_a = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"A[{i}][{j}]: ")))
    matrix_a.append(row)

print("Enter elements for Matrix B:")
matrix_b = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"B[{i}][{j}]: ")))
    matrix_b.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

print("Resulting Matrix after Addition:")
for row in result:
    print(row)