# Hàm đệ quy để tính giai thừa
def factorial(n):
    if n == 0 or n == 1:  # Điều kiện dừng
        return 1
    else:
        return n * factorial(n - 1)  # Gọi đệ quy

# Yêu cầu người dùng nhập vào một số
number = int(input("Nhập vào một số không âm để tính giai thừa: "))

# Kiểm tra số nhập vào có hợp lệ hay không
if number < 0:
    print("Vui lòng nhập một số không âm!")
else:
    result = factorial(number)  # Gọi hàm tính giai thừa
    print(f"Giai thừa của {number} là: {result}")