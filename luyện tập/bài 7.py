class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, person_string):
        """Tạo đối tượng Person từ chuỗi 'name-age'."""
        name, age_str = person_string.split('-')
        return cls(name, int(age_str))  # Chuyển đổi age_str thành số nguyên

    def __str__(self):
        """Trả về chuỗi mô tả đối tượng Person."""
        return f"Name: {self.name}, Age: {self.age}"

# Ví dụ sử dụng
person_string = "Nu-18"
person = Person.from_string(person_string)

# In ra thông tin của đối tượng Person
print(person)