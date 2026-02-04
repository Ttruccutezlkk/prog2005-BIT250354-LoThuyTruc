# Khởi tạo mật khẩu
correct_password = "ttruc123"
password = ""

# Sử dụng vòng lặp while để yêu cầu người dùng nhập mật khẩu
while password != correct_password:
    password = input("Nhập mật khẩu: ")  # Yêu cầu người dùng nhập mật khẩu
    if password != correct_password:
        print("Mật khẩu không đúng. Vui lòng thử lại.")

print("Mật khẩu đúng! Truy cập thành công.")