# Hàm đệ quy để tính tổng
def sum_recursive(n):
    if n == 1:  # Điều kiện dừng
        return 1
    else:
        return n + sum_recursive(n - 1)  # Gọi đệ quy

# Yêu cầu người dùng nhập vào một số nguyên dương
n = int(input("Nhập vào một số nguyên dương n: "))

# Kiểm tra xem n có hợp lệ hay không
if n < 1:
    print("Vui lòng nhập một số nguyên dương!")
else:
    result = sum_recursive(n)  # Gọi hàm tính tổng
    print(f"Tổng của tất cả các số nguyên từ 1 đến {n} là: {result}")