"""Nhập vào một giá trị độ C, in ra giá trị độ F tương ứng
, biết F = (9.0/5.0 x C) + 32"""

try :
    doC = float(input("Nhập vào giá trị độ C: "))
    if doC < 273.15:
        print("Giá trị nhiệt độ không thỏa mãn")
    else:
        doF = (9.0/5.0 * doC) + 32
        print(f"Độ F tương ứng với {doC} độ C là: {doF:.2f}")
except ValueError:
    print("Vui lòng nhập độ là dạng số")