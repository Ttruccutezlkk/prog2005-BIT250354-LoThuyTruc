def count_characters(input_string):
    upper_case_count = 0
    lower_case_count = 0
    digit_count = 0
    special_count = 0
    whitespace_count = 0
    vowels_count = 0
    consonants_count = 0

    vowels = "aeiouAEIOU"

    for char in input_string:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char.isspace():
            whitespace_count += 1
        else:
            special_count += 1

        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1

    print("Số lượng chữ cái in hoa:", upper_case_count)
    print("Số lượng chữ cái in thường:", lower_case_count)
    print("Số lượng chữ số:", digit_count)
    print("Số lượng ký tự đặc biệt:", special_count)
    print("Số lượng ký tự khoảng trắng:", whitespace_count)
    print("Số lượng nguyên âm:", vowels_count)
    print("Số lượng phụ âm:", consonants_count)

# Nhập chuỗi từ người dùng
input_string = input("Nhập một chuỗi: ")
count_characters(input_string)
