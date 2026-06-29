rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements for the Matrix:")
matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input(f"Element[{i}][{j}]: ")))
    matrix.append(row)

for j in range(cols):
    col_sum = 0
    for i in range(rows):
        col_sum += matrix[i][j]
    print(f"Sum of Column {j + 1}: {col_sum}")