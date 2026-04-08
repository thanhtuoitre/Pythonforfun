"""Viết chương trình nhập n số, xoá số thứ k trong n số vừa nhập.
In ra n-1 số còn lại"""

try:
    n = int(input("Nhập vào n phần tử:"))
    a = []

    if n>0:
        for i in range(n):
            a.append(float(input("Nhập vào phần tử thứ %d:" %(i+1))))

        print("Dãy vừa nhập là",a)

        k = int(input("Nhập vào số thứ k muốn xóa trong dãy:"))

        if 0<k<=len(a):
            del a[k-1]
            print("Dãy sau khi xóa ",a)
        else:
            print("Nhập sai giá trị k")
    else:
        print("Nhập sai giá trị n.n phải là số nguyên dương")

except ValueError:
    print("Nhập sai kiểu dữ liệu n")