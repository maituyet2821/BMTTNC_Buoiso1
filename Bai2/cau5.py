def demsolan(lst):
    count_dict = {}
    for item in lst:
        if item in count_dict:
            count_dict[item]+=1
        else:
            count_dict[item]=1
    return count_dict
input_string = input("Nhập dánh sách các từ, cách nhau bằng dấu cách: ")
word_list=input_string.split()
so_lan=demsolan(word_list)
print("Số lần xuất hiện của các phần tử:", so_lan)