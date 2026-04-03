""" Nhập vào một số nguyên không âm,
kiểm tra xem nó có phải là số nguyên tố hay không?"""

n = int(input("Nhập vào số n: "))
if n < 0:
    print("Nhập sai rồi bạn")
else:
    la_nguyen_to = 0
    for i in range(1,n+1):
        if (n % 1 == 0):
            la_nguyen_to = True
            print("n là số nguyên tố")
        else:
            print("n không phải là số nguyên tố")
