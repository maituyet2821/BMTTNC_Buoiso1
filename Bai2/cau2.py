def daonguoclist(lst):
    return lst[::-1]
input_list=input("Nhập sanh sách các số, cách nhau bằng dấu phẩy: ")
numbers=list(map(int, input_list.split(',')))
list_dao_nguoc=daonguoclist(numbers)
print("List sau khi đảo ngược:", list_dao_nguoc)