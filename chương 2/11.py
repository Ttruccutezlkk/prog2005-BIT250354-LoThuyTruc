# Yêu cầu người dùng nhập vào điểm trung bình
average_score = float(input("Nhập vào điểm trung bình: "))

# Kiểm tra và in ra xếp loại
if average_score >= 8:
    print("Xếp loại: Giỏi")
elif 6.5 <= average_score < 8:
    print("Xếp loại: Khá")
elif 5.0 <= average_score < 6.5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")