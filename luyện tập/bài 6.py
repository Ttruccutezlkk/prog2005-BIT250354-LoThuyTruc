class Product:
    def __init__(self, price):
        self._price = price  # Khởi tạo thuộc tính _price qua constructor

    @property
    def price(self):
        """Getter cho thuộc tính price."""
        return self._price

    @price.setter
    def price(self, value):
        """Setter cho thuộc tính price, chỉ cho phép giá trị lớn hơn 0."""
        if value > 0:
            self._price = value
        else:
            raise ValueError("Giá phải lớn hơn 0.")

    def __str__(self):
        """Trả về thông tin về giá sản phẩm."""
        return f"Giá sản phẩm: {self._price}"

# Khởi tạo đối tượng Product và in ra giá
product = Product(150.0)
print(product)  # In ra giá sản phẩm

# Thay đổi giá sản phẩm
product.price = 200.0
print(product)  # In ra giá sản phẩm đã thay đổi

