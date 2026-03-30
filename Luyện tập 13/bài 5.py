class Flower:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return "Hoa: " + self.name + ", Màu: " + self.color

hoa1 = Flower("Hoa hồng", "Đỏ")

print(hoa1)