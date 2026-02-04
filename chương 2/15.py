# Yêu cầu người dùng nhập vào một số nguyên dương
number = int(input("Nhập vào một số nguyên dương: "))

# Khởi tạo biến tổng
sum_of_digits = 0

# Sử dụng vòng lặp while để tính tổng các chữ số
while number > 0:
    digit = number % 10  # Lấy chữ số cuối cùng
    sum_of_digits += digit  # Cộng chữ số vào tổng
    number //= 10  # Bỏ chữ số cuối cùng

# In ra kết quả
print(f"Tổng các chữ số là: {sum_of_digits}")