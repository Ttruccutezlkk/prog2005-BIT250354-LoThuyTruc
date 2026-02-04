# Yêu cầu người dùng nhập vào một số nguyên dương 5 chữ số
number = input("Nhập vào một số nguyên dương 5 chữ số: ")

# Kiểm tra xem số nhập vào có phải là số nguyên dương 5 chữ số hay không
if number.isdigit() and len(number) == 5:
    # Tìm chữ số lớn nhất trong số
    max_digit = max(number)  # max() sẽ tìm ký tự lớn nhất
    print(f"Chữ số lớn nhất trong số {number} là: {max_digit}")
else:
    print("Vui lòng nhập một số nguyên dương 5 chữ số hợp lệ!")