"""Viết chương trình tìm giá trị lớn nhất
trong 3 số nguyên nhập vào từ bàn phím"""

try:
    so1 = int(input("Nhập vào giá trị số thứ nhất: "))
    so2 = int(input("Nhập vào giá trị số thứ hai: "))
    so3 = int(input("Nhập vào giá trị số thứ ba: "))

    print("Số có giá trị lớn nhất là",max(so1,so2,so3))
except ValueError:
    print("Nhập sai kiểu giá trị. Vui lòng thử lại!")