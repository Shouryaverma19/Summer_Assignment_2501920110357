rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for the Matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element[{i}][{j}]: ")))
    matrix.append(row)

transpose = []
for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transposed Matrix:")
for row in transpose:
    print(row)