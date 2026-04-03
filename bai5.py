"""Viết chương trình nhập n số, xoá số thứ k trong n số vừa nhập.
In ra n-1 số còn lại"""

n = int(input("Nhập vào n:"))
a = []

for i in range(n):
    a.append(float(input("Nhập vào số thứ %d: " % (i + 1))))

print("Dãy số vừa nhập", a)

k = int(input("Nhập vào số muốn xóa k:"))

if 0 <= 0 <= len(a):
    del a[k - 1]
    print("Dãy a sau khi xóa ", a)
else:
    print("k ko hợp lệ bạn")
