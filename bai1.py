"""
1.	Nhập vào một giá trị độ C, in ra giá trị độ F tương ứng, biết F = (9.0/5.0 x C) + 32
"""

doC = float(input("Nhập vào độ C:"))
doF = (9.0/5.0 * doC ) + 32
print(f"Độ F tương ứng với {doC} là: {doF:.2f}")