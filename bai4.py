"""Viết chương trình nhập vào dãy A gồm n phần tử và
in ra dãy số được sắp xếp theo thứ tự tăng dần."""

n = int(input("Nhập vào n:"))

a = []
tg = 0

for i in range(n):
    a.append(float(input("Nhập số thứ %d:" % (i + 1))))

print("Các phần tử được nhập là: ", a)

a.sort()

print("Các phần tử sau khi được sắp xếp tăng dần là: ", a)
