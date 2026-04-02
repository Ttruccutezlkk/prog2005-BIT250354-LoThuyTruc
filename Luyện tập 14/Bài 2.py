n = int(input("Nhap n = "))

print("\nHinh 1:")
for i in range(n):
    print("* " * n)


print("\nHinh 2:")
for i in range(1, n + 1):
    print("* " * i)


print("\nHinh 3:")
for i in range(n, 0, -1):
    print("* " * i)

print("\nHinh 4:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)


print("\nHinh 5:")
for i in range(1, n+1):
    for j in range(1, i+1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHinh 6:")
for i in range(n, 0, -1):
    for j in range(1, i+1):
        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHinh 7:")
for i in range(1, n + 1):

    print("  " * (n - i), end="")

    for j in range(1, i + 1):

        if i == n or j == 1 or j == i:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("\nHinh 8:")
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print("\nHinh 9:")
for i in range(1, n + 1):
    khoang_trang_ngoai = "  " * (n - i)
    if i == 1:
        print(khoang_trang_ngoai + "*")
    elif i == n:
        print("* " * (2 * n - 1))
    else:
        khoang_trang_trong = "  " * (2 * i - 3)
        print(khoang_trang_ngoai + "* " + khoang_trang_trong + "*")

print("\nHinh 10:")
for i in range(n, 0, -1):
    khoang_trang_ngoai = "  " * (n - i)
    if i == 1:
        print(khoang_trang_ngoai + "*")
    elif i == n:
        print("* " * (2 * n - 1))
    else:
        khoang_trang_trong = "  " * (2 * i - 3)
        print(khoang_trang_ngoai + "* " + khoang_trang_trong + "*")