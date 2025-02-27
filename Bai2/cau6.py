def xoa(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        return True
    else:
        return False
my_dict = {'a':1, 'b':2, 'c':3, 'd':4}
key_to_delete = 'b'
result = xoa(my_dict, key_to_delete)
if result:
    print(":Phần từ đã được xóa từ Dictionary:", my_dict)
else:
    print("Không tìm thấy phần tử cần xóa trong Dictionary.")