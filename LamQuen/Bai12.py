"""import math
def checkSNT(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_four_primes(n):
    if n < 4:
        return None
    for i in range(2, n - 3):
        if ([i]+[i+i]+[i+2]+[i+3] <=n) and checkSNT([i]+[i+i]+[i+2]+[i+3]):
            return ([i],[i+1],[i+2],[i+3])
    return None

n = int(input("Nhập số N: "))
result = find_four_primes(n)
if (find_four_primes):
    print("Bốn số nguyên tố liên tiếp tìm được là: " , result)
else:
    print("Không tìm thấy bốn số nguyên tố liên tiếp phù hợp")
    """
#Hàm is_prime trả về True nếu một số là số nguyên tố, 
# và False nếu không. Hàm find_four_primes tìm bốn số nguyên tố liên tiếp 
# theo cách duyệt từ 2 đến N-4, 
# kiểm tra xem có bốn số liên tiếp là số nguyên tố và tổng của chúng là số nguyên tố hay không. 
# Nếu tìm thấy bốn số nguyên tố liên tiếp phù hợp, hàm trả về bốn số nguyên tố, ngược lại trả về None.



def checkSNT(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

"""def find_prime_sum(n):
    primes = [2]
    for i in range(3, n + 1):
        if checkSNT(i):
            primes.append(i)

    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            for k in range(j + 1, len(primes)):
                for l in range(k+1, len(primes)):
                    if primes[i] + primes[j] + primes[k] + primes[l]<= n and checkSNT(primes[i] + primes[j] + primes[k]+primes[l]):
                        return primes[i], primes[j], primes[k],primes[l]
"""
def tinhTong(N):
    for i in range(2, N):
        if checkSNT(i):
            for j in range(i+1, N):
                if checkSNT(j):
                    for k in range(j+1, N):
                        if checkSNT(k):
                            for l in range(k+1, N):
                                if checkSNT(l):
                                    if checkSNT(i+j+k+l):
                                        return (i, j, k, l)
    return None
n = int(input("Enter a number: "))
result = tinhTong(n)
if result:
    print("Bốn số đó là:", n, ":", result)
else:
    print("Không có só nào", n)


"""
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_consecutive_prime_sum(n):
    primes = [2]
    for i in range(3, n + 1):
        if is_prime(i):
            primes.append(i)

    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            for k in range(j + 1, len(primes)):
                for l in range(k + 1, len(primes)):
                    if primes[i] + primes[j] + primes[k] + primes[l] <= n and is_prime(primes[i] + primes[j] + primes[k] + primes[l]):
                        return [primes[i], primes[j], primes[k], primes[l]]

n = int(input("Enter a number: "))
result = find_consecutive_prime_sum(n)
if result:
    print("Four consecutive prime numbers with sum less than or equal to", n, ":", result)
else:
    print("No four consecutive prime numbers found with sum less than or equal to", n)

"""

