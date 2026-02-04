# Yêu cầu người dùng nhập vào một số nguyên dương
n = int(input("Nhập vào một số nguyên dương: "))

# Kiểm tra số nhập vào có hợp lệ hay không
if n <= 1:
    print(f"{n} không phải là số nguyên tố.")
else:
    is_prime = True  # Giả sử là số nguyên tố
    for i in range(2, int(n**0.5) + 1):  # Lặp từ 2 đến căn bậc hai của n
        if n % i == 0:  # Nếu n chia hết cho i
            is_prime = False  # Không phải số nguyên tố
            break  # Dừng vòng lặp

    if is_prime:
        print(f"{n} là số nguyên tố.")
    else:
        print(f"{n} không phải là số nguyên tố.")