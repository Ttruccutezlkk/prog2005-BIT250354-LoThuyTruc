# Yêu cầu người dùng nhập vào một số
number = input("Nhập vào một số: ")

# Khởi tạo biến tổng
sum_of_digits = 0

# Duyệt qua từng ký tự trong số đã nhập
for digit in number:
    if digit.isdigit():  # Kiểm tra xem ký tự có phải là số không
        sum_of_digits += int(digit)  # Chuyển ký tự thành số và cộng vào tổng

# In ra kết quả
print(f"Tổng các chữ số của số {number} là: {sum_of_digits}")