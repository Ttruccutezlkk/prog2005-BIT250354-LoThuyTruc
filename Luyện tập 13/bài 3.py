tong = 0
print("Các số chẵn từ 1 đến 20 là:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")
        tong = tong + i
print("\nTổng các số chẵn là:", tong)