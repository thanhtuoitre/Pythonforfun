"""Viết chương trình nhập mảng gồm n phần tử.
Số nguyên dương n được nhập từ bàn phím.
In ra mảng và tính tổng các phần tử"""

n = int(input("Nhập n: "))
if n<=0:
    print("Phải nhập số tự nhiên")
else:
    a= []
    tong=0
    for i in range(n):
        a.append(float(input("Nhập số thứ %d: "%(i+1))))
        tong = tong + a[i]
    print(a)
    print("Tổng các số vừa nhập xong là: ",tong)


