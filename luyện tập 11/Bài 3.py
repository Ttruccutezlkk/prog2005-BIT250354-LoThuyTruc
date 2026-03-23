s = input("Nhập số: ")
b = s.split()

tong = 0

print("Số chẵn là:")

for i in b:
    so = int(i)
    if so % 2 == 0:
        print(so)
        tong = tong + so

print("Tổng là:", tong)