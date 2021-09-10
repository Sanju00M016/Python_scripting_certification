x_row = int(input("Enter the Number of Rows: "))
y_col = int(input("Enter the Number Columns: "))

mul_list = [[0 for col in range(y_col)] for row in range(x_row)]

for row in range(x_row):
    for col in range(y_col):
        mul_list[row][col] = row * col
print(mul_list)