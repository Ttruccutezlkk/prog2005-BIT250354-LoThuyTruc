import csv

name = input("Tên: ")
age = input("Tuổi: ")
id = input("ID: ")

# Ghi file txt
with open("nhanvien.txt", "w", encoding="utf-8") as f:
    f.write(name + "," + age + "," + id)

# Ghi file csv
with open("nhanvien.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Tên", "Tuổi", "ID"])
    writer.writerow([name, age, id])

print("Đã lưu file")