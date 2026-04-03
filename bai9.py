"""Nhập vào một mảng n số nguyên dương,
đếm và in ra các số chia hết cho cả 2 và 5,
tính trung bình các số đó"""

n = int(input("Nhập vào n:"))
a = []
tong = 0
tbc = 0
dem = 0

for i in range(n):
    a.append(float(input("Nhập số thứ %d:" % (i + 1))))
print("Mảng vừa nhập là", a)

for i in range(n):
    if a[i] % 2 == 0 and a[i] % 5 == 0:
        tong = tong + a[i]
        dem = dem + 1
print("Trung binh cong cac so do la: ", tong / dem)
