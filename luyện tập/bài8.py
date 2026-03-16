class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # nạp chồng toán tử +
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x, new_y)

# tạo 2 vector
v1 = Vector(2, 3)
v2 = Vector(4, 5)

# cộng 2 vector
v3 = v1 + v2

# in kết quả
print("Vector mới:", v3.x, v3.y)