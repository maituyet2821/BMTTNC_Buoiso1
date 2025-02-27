def truycap(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element

input_tuple = eval(input("Nhập tuple, ví dụ(1, 2, 3): "))
first, last = truycap(input_tuple)
print("Phần tử đầu tiên:", first)
print("Phẩn tử cuối cùng:", last)