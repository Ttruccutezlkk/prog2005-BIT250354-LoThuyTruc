# Yêu cầu người dùng nhập vào số nguyên dương n
n = int(input("Nhập vào một số nguyên dương n: "))

# Khởi tạo biến tổng
sum_of_odds = 0

# Sử dụng vòng lặp for để tính tổng các số lẻ từ 1 đến n
for i in range(1, n + 1):  # Lặp từ 1 đến n
    if i % 2 != 0:  # Kiểm tra xem i có phải là số lẻ không
        sum_of_odds += i  # Cộng số lẻ vào tổng

# In ra kết quả
print(f"Tổng các số lẻ từ 1 đến {n} là: {sum_of_odds}")