def kiemtra(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True
number = int(input("Nhập vào các số cần kiểm tra: "))
if kiemtra(number):
    print(number, "là số nguyên số.")
else:
    print(number, "không phải là số nguyên số.")