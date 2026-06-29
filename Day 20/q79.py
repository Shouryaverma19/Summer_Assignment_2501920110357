rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for the Matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element[{i}][{j}]: ")))
    matrix.append(row)

for i in range(rows):
    row_sum = 0
    for j in range(cols):
        row_sum += matrix[i][j]
    print(f"Sum of Row {i + 1}: {row_sum}")