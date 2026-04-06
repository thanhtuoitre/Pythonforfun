"""Viết chương trình nhập vào dãy A gồm n phần tử và
in ra dãy số được sắp xếp theo thứ tự tăng dần."""

try:
    n = int(input("Nhập vào n phần tử:"))
    if n > 0:
        a = []
        for i in range(n):
            a.append(float(input("Nhập vào phần tử thứ %d :"%(i+1))))

        print("Dãy a vừa nhập là",a)

        a.sort()
        print("Dãy a sau khi được sắp xếp theo thứ tự tăng dần:",a)
    else:
        print("n phải là số nguyên dương")

except ValueError:
    print("Nhập sai kiểu giá trị!")