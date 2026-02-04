# Yêu cầu người dùng nhập vào một số trong khoảng từ 1 đến 9
number = int(input("Nhập một số từ 1 đến 9: "))

# Kiểm tra xem số nhập vào có hợp lệ không
if 1 <= number <= 9:
    print(f"Bảng cửu chương của {number}:")
    for i in range(1, 10):
        print(f"{number} x {i} = {number * i}")
else:
    print("Vui lòng nhập số trong khoảng từ 1 đến 9.")