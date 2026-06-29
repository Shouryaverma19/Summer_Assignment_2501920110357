n = int(input("Enter the size of the square matrix (N x N): "))

print("Enter elements for the Matrix:")
matrix = []
for i in range(n):
    row = []
    for j in range(n):
        row.append(int(input(f"Element[{i}][{j}]: ")))
    matrix.append(row)

is_symmetric = True
for i in range(n):
    for j in range(n):
        if matrix[i][j] != matrix[j][i]:
            is_symmetric = False
            break

if is_symmetric:
    print("The matrix is Symmetric.")
else:
    print("The matrix is not Symmetric.")