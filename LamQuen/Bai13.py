import math
def checkSNT(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def duyetSNT(n):
    for i in range(2, n):
        if checkSNT(i) and checkSNT(n - i):
            return (i, n - i)
    return None

n = int(input("Nhập số N: "))
result = duyetSNT(n)
if result:
    print(f"Hai số nguyên tố tìm được là: {result[0]} và {result[1]}")
else:
    print("Không tìm thấy hai số nguyên tố phù hợp")
#Hàm is_prime trả về True nếu một số là số nguyên tố, 
# và False nếu không. Hàm find_two_primes 
# tìm hai số nguyên tố phù hợp theo cách duyệt từ 2 đến N-2, 
# kiểm tra xem cả hai số là số nguyên tố hay không. 
# Nếu tìm thấy hai số nguyên tố, hàm trả về hai số nguyên tố, ngược lại trả về None.




