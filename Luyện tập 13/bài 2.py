chuoi = input("Nhập chuỗi: ")

do_dai = len(chuoi)
print("Độ dài chuỗi là:", do_dai)

dem = 0
for i in chuoi:
    if i == 'a':
        dem = dem + 1

print("Số ký tự a là:", dem)