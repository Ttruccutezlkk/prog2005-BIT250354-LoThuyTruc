import math

so = float(input("Nhập một số: "))

if so < 0:
    print("Lỗi: không tính được căn bậc hai của số âm")
else:
    can = math.sqrt(so)
    print("Căn bậc hai là:", can)