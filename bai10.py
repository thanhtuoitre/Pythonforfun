"""	Nhập vào chiều dài 3 cạnh một tam giác,
kiểm tra tính hợp lệ của 3 giá trị nhập vào,
nếu hợp lệ, tính diện tích và chu vi tam giác"""
import math

a = float(input("Nhập vào cạnh a:"))
b = float(input("Nhập vào cạnh b:"))
c = float(input("Nhập vào cạnh c:"))

if (a + b < c) or (a + c < b) or (b + c < a):
    print("Bạn nhập sai rồi")
else:
    chuvi = a + b + c
    dientich = math.sqrt(chuvi/2*(chuvi/2-a)*(chuvi/2-b)*(chuvi/2-c))
    print("Chu vi của tam giác là: ",chuvi)
    print("Diện tích của tam giác là: ",dientich)
