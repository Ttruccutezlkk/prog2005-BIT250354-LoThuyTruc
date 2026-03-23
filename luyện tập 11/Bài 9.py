def input_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Nhập hàng thứ {i + 1} (các giá trị cách nhau bằng dấu cách): ")
            if not row.strip():  # Kiểm tra giá trị trống
                print("Lỗi: Không được nhập giá trị trống. Vui lòng nhập lại.")
                continue
            matrix.append(list(map(int, row.split())))
            break
    return matrix


def add_matrices(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])
    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = mat1[i][j] + mat2[i][j]

    return result


# Nhập kích thước ma trận
rows = int(input("Nhập số hàng của ma trận: "))
cols = int(input("Nhập số cột của ma trận: "))

print("Nhập ma trận thứ nhất:")
matrix1 = input_matrix(rows, cols)

print("Nhập ma trận thứ hai:")
matrix2 = input_matrix(rows, cols)

# Cộng hai ma trận
result_matrix = add_matrices(matrix1, matrix2)

# In kết quả
print("Kết quả của phép cộng hai ma trận là:")
for row in result_matrix:
    print(" ".join(map(str, row)))