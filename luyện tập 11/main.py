arr = []
for i in range(5):
    s = input("Nhập chuỗi thứ " + str(i+1) + ": ")
    arr.append(s)

for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1

    # Dịch chuyển phần tử
    while j >= 0 and len(arr[j]) < len(key):
        arr[j + 1] = arr[j]
        j = j - 1

    arr[j + 1] = key

    # In từng bước
    print("Bước", i, ":", arr)