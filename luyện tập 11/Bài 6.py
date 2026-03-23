n = int(input("Nhập số người: "))
d = {}

for i in range(n):
    name = input("Tên: ")
    age = int(input("Tuổi: "))
    d[name] = age

# Tính trung bình
tong = 0
for i in d:
    tong += d[i]

print("Tuổi trung bình:", tong / n)

# Đưa về list để sort
items = list(d.items())

# Selection Sort giảm dần theo tuổi
for i in range(len(items)):
    max_idx = i
    for j in range(i+1, len(items)):
        if items[j][1] > items[max_idx][1]:
            max_idx = j

    items[i], items[max_idx] = items[max_idx], items[i]

print("Sau khi sắp xếp:")
for i in items:
    print(i)