"""
1.	Viết chương trình nhập mảng gồm n phần tử.
Số nguyên dương n được nhập từ bàn phím.
In ra mảng và tính tổng các phần tử
"""

n = int(input("Nhập vào n phần tử của mảng:"))
a = []
tong = 0

if n > 0:
    for i in range(n):
        a.append(float(input("Nhập vào phần tử thứ: %d:" % (i + 1))))
        tong = tong + a[i]
else:
    print("Bạn nhập sai giá trị rồi")

print("Dãy số bạn vừa nhập là:",a)
print(f"Tổng của dãy số vừa nhập: {tong}")