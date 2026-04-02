n = int(input("Nhap n = "))


print("\nHinh 1:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(1, end=" ")
    print()


print("\nHinh 2:")
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end=" ")
    print()


print("\nHinh 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("\nHinh 4:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


print("\nHinh 5:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i or i == n:
            print(j, end=" ")
        else:
            print(" ", end=" ")
    print()


print("\nHinh 6:")
for i in range(n, 0, -1):
    for j in range(1, i + 1):

        if i == n or j == 1 or j == i:
            print(j, end=" ")
        else:
            print("  ", end="")
    print()


print("\nHinh 7:")
for i in range(1, n + 1):

    print("  " * (n - i), end="")

    for j in range(1, i + 1):

        print(i, end="   ")

    print()

print("\nHinh 8:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")

    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()


print("\nHinh 9:")
for i in range(1, n + 1):
    print("  " * (n - i), end="")
    for j in range(1, 2 * i):

        if j == 1:
            print(1, end=" ")
        elif j == 2 * i - 1:
            if i == 1: pass
            else: print(1, end=" ")
        elif i == n:

            val = j if j <= n else 2 * n - j
            print(val, end=" ")
        else:
            print(" ", end=" ")
    print()