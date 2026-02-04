number = int(input("Nhập vào một số dương: "))

# Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n <= 1:
        return False  # Các số <= 1 không phải là số nguyên tố
    for i in range(2, int(n**0.5) + 1):  # Kiểm tra từ 2 đến căn bậc hai của n
        if n % i == 0:  # Nếu n chia hết cho i
            return False  # N không phải là số nguyên tố
    return True  # N là số nguyên tố

# Kiểm tra và in kết quả
if is_prime(number):
    print(f"{number} là số nguyên tố.")
else:
    print(f"{number} không phải là số nguyên tố.")