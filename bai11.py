"""Viết chương trình nhập vào giá trị tháng, năm,
cho biết tháng đó có bao nhiêu ngày."""

import calendar

thang = int(input("Nhập vào tháng:"))
nam = int(input("Nhập vào năm:"))

if thang<=0 or thang>12:
    print("Nhập lại đi bạn")
else:
    ngay = calendar.monthrange(nam,thang)[1]
    print(f"Tháng {thang} Năm {nam} có {ngay} ngày.")