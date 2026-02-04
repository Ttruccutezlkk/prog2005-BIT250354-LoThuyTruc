# Yêu cầu người dùng nhập vào một số dương
number = input("Nhập vào một số dương: ")

# Kiểm tra xem số nhập vào có phải là số dương không
if number.isdigit():  # Kiểm tra nếu tất cả các ký tự đều là chữ số
    # Đảo ngược các chữ số của số
    reversed_number = number[::-1]
    print(f"Số đảo ngược của {number} là: {reversed_number}")
else:
    print("Vui lòng nhập một số dương hợp lệ!")