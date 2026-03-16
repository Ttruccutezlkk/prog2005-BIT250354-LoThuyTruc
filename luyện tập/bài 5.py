class User:
    def __init__(self, user_id):
        self._id = user_id  # Sử dụng _id để chỉ định id trong lớp

    @property
    def id(self):
        """Chỉ cho phép đọc thuộc tính id."""
        return self._id

# Ví dụ sử dụng lớp User
user = User(12345)
print(user.id)  # In ra giá trị id: 12345
