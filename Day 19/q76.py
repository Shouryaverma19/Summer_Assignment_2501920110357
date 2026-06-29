n = int(input("Enter the size of the square matrix (N x N): "))

print("Enter elements for the Matrix:")
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Element[{i}][{j}]: ")))
    matrix.append(row)

diagonal_sum = 0
for i in range(n):
    diagonal_sum += matrix[i][i]

print("The sum of the primary diagonal elements is:", diagonal_sum)