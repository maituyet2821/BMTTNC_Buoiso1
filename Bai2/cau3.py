def tao_tuple(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, cách nhau bởi dấu phẩy: ")
numbers=list(map(int, input_list.split(',')))

my_tuple=tao_tuple(numbers)
print("List: ",numbers)
print("Tuple từ List:", my_tuple)