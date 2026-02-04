# Yêu cầu người dùng nhập vào hai số nguyên dương
num1 = int(input("Nhập vào số nguyên dương thứ nhất: "))
num2 = int(input("Nhập vào số nguyên dương thứ hai: "))

# Kiểm tra xem các số nhập vào có phải là số nguyên dương hay không
if num1 <= 0 or num2 <= 0:
    print("Vui lòng nhập hai số nguyên dương!")
else:
    # Giả sử ƯCLN là 1
    gcd = 1

    # Tìm ƯCLN bằng cách sử dụng vòng lặp
    for i in range(1, min(num1, num2) + 1):  # Lặp từ 1 đến số nhỏ hơn trong hai số
        if num1 % i == 0 and num2 % i == 0:  # Kiểm tra xem i có phải là ước số chung không
            gcd = i  # Cập nhật ƯCLN

    print(f"Ước số chung lớn nhất của {num1} và {num2} là: {gcd}")