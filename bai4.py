"""
Viết chương trình nhập n số, xoá số thứ k trong n số vừa nhập. In ra n-1 số còn lại
"""

n = int(input("Nhập vào n: "))
a = []

if n > 0:
    for i in range(n):
        a.append(input("Nhập vào phần tử thứ %d: "%(i+1)))
    print("Dãy số bạn vừa nhập là ",a)
else:
    print("Bạn nhập sai rồi")

k = int(input("Nhập vào phần tử k muốn xóa:"))
if k<0 or k>len(a):
    print("Bạn nhập sai giá trị k")
else:
    del a[k-1]
    print("Dãy số sau khi xóa",a)


