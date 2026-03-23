def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid  # Trả về chỉ số khi tìm thấy
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Trả về -1 nếu không tìm thấy

# Danh sách các chuỗi đã được sắp xếp
strings = ["Cocacola", "Bưởi 5 Roi", "Bia 333", "Lê Hoành Sử", "Nguyễn Khánh Sơn"]

# Nhập chuỗi từ bàn phím
search_string = input("Nhập chuỗi muốn tìm: ")

# Tìm kiếm chuỗi
result = binary_search(strings, search_string)

# In kết quả
if result != -1:
    print(f"Chuỗi '{search_string}' được tìm thấy ở vị trí: {result}")
else:
    print(f"Chuỗi '{search_string}' không có trong danh sách.")