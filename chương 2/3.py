# Yêu cầu người dùng nhập vào số n
n = int(input("Nhập vào một số n để in ra n số đầu tiên trong dãy Fibonacci: "))

# Hàm để tính dãy Fibonacci
def fibonacci(n):
    fib_sequence = []  # Danh sách chứa dãy Fibonacci
    a, b = 0, 1  # Hai số đầu tiên trong dãy Fibonacci
    for _ in range(n):
        fib_sequence.append(a)  # Thêm số hiện tại vào danh sách
        a, b = b, a + b  # Cập nhật a và b cho số tiếp theo
    return fib_sequence

# In ra dãy Fibonacci
if n > 0:
    print(f"N số đầu tiên trong dãy Fibonacci là: {fibonacci(n)}")
else:
    print("Vui lòng nhập một số dương.")