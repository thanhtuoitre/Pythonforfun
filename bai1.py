"""Nhập vào một giá trị độ C, in ra giá trị độ F tương ứng, biết F = (9.0/5.0 x C) + 32"""

print("Nhập vào độ C:")
C = float(input())
doF: float = (9.0 / 5.0 * C)
print(f"Độ F vừa tính được là :{doF:.2f}")
