"""
Viết chương trình nhập vào dãy A gồm n phần tử và in ra dãy số được sắp xếp theo thứ tự tăng dần.
"""

n = int(input("Nhập vào n phần tử:"))
a = []

if n > 0:
    for i in range(n):
        a.append(input("Nhập vào phần tử thứ %d :"%(i+1)))
    print("Dãy số bạn vừa nhập vào là:",a)
    a.sort()
    print("Dãy số sau khi được sắp xếp theo thứ tự tăng dần:",a)
else:
    print("Bạn nhập sai giá trị n rồi")


