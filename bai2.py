"""Viết chương trình nhập mảng gồm n phần tử.
Số nguyên dương n được nhập từ bàn phím.
In ra mảng và tính tổng các phần tử"""

a = []
tong = 0
try:
    n = int(input("Nhập vào n phần tử: "))
    if n>0:
        for i in range(n):
            a.append(float(input("Nhập vào giá trị phần tử thứ %d:" %(i+1))))
            tong += a[i]

        print("Dãy số vừa nhập là:",a)
        print("Tổng dãy số vừa nhập: ",tong)
    else:
        print("Nhập sai giá trị của n, n phải là số nguyên dương")
except ValueError:
    print("Nhập sai kiểu giá trị của n.Vui lòng nhập lại!")