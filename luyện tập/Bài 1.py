def tinh_bmi():
    weight = float(input("Nhập cân nặng (kg): "))
    height = float(input("Nhập chiều cao (m): "))

    bmi = weight / (height * height)

    print(f"Chỉ số khối cơ thể (BMI) của bạn là: {bmi:.2f}")

tinh_bmi()