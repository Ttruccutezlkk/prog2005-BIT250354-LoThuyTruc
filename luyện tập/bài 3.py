# Hàm chuẩn hóa tên người dùng
def chuan_hoa_ten():
    # Nhập tên từ người dùng
    ten = input("Nhập tên người dùng: ")

    # Bước 1: Loại bỏ khoảng trắng thừa ở đầu và cuối
    ten = ten.strip()

    # Bước 2: Chia tên thành các từ
    danh_sach_tu = ten.split()

    # Bước 3: Viết hoa chữ cái đầu mỗi từ
    danh_sach_tu = [tu.capitalize() for tu in danh_sach_tu]

    # Bước 4: Kết hợp lại thành một chuỗi với một khoảng trắng giữa các từ
    ten_chuan_hoa = ' '.join(danh_sach_tu)

    # Hiển thị tên đã chuẩn hóa
    print(f"Tên đã chuẩn hóa: {ten_chuan_hoa}")


# Gọi hàm để thực hiện
chuan_hoa_ten()