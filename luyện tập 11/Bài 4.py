# Khởi tạo
lst = [1, 2, 3, 4, 5]

# Thêm phần tử
x = int(input("Nhập phần tử thêm: "))
lst.append(x)

# Đếm số lần xuất hiện
k = int(input("Nhập k: "))
count = 0
for i in lst:
    if i == k:
        count += 1
print("Số lần xuất hiện:", count)

# Hàm kiểm tra nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Tính tổng số nguyên tố
tong = 0
for i in lst:
    if is_prime(i):
        tong += i

print("Tổng số nguyên tố:", tong)

# Sắp xếp
lst.sort()
print("Danh sách sau sắp xếp:", lst)

# Xóa
lst.clear()
print("Danh sách sau khi xóa:", lst)