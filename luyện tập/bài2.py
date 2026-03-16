def tong_cac_chu_so():
    number = input("Nhập vào một số: ")

    tong = 0

    for chu_so in number:
        if chu_so.isdigit():  # Kiểm tra xem ký tự có phải là số không
            tong += int(chu_so)  # Chuyển ký tự thành số nguyên và cộng vào tổng

    print(f"Tổng các chữ số của số {number} là: {tong}")

tong_cac_chu_so()