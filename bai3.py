"""Viết chương trình tìm giá trị lớn nhất
trong 3 số nguyên nhập vào từ bàn phím"""

print("Nhập vào số nguyên thứ nhất: ")
so1 = int(input())

print("Nhập vào số nguyên thứ hai: ")
so2 = int(input())

print("Nhập vào số nguyên thứ ba: ")
so3 = int(input())
1
solonnhat = 0

if so1<so2 and so2<so3:
    max = so3
elif so1>so2 and so1<so3:
    max = so2
else:
    max = so1

print(f"Số lớn nhất là {max}")
