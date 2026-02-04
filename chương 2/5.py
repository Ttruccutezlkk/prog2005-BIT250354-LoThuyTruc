# Yêu cầu người dùng nhập vào chuỗi
user_string = input("Nhập vào một chuỗi: ")

# Yêu cầu người dùng nhập vào ký tự cần đếm
character = input("Nhập vào một ký tự: ")

# Kiểm tra xem người dùng có nhập một ký tự hay không
if len(character) == 1:
    # Sử dụng phương thức count để đếm số lần xuất hiện của ký tự trong chuỗi
    count = user_string.count(character)
    print(f"Ký tự '{character}' xuất hiện {count} lần trong chuỗi.")
else:
    print("Vui lòng nhập một ký tự hợp lệ.")