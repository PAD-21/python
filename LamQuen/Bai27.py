"""def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
"""
def gcd(a,b):
    if a<=0:
        a=-a
    if b<=0:
        b=-b
    if a==0 or b==0:
        return a+b
    while(a!=b):
        if(a>b):
            a=a-b
        elif(b>a):
            b=b-a
        return a
    
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for a in range(1, 1000):
    for b in range(a+1, 1000):
        if  is_prime(gcd(a, b)):
            print((a,b))
            break

#a=int(input("Nhập a:"))
#b=int(input("Nhập b:"))

#Ở đây, hàm gcd(a, b) được sử dụng để tính GCD của hai số a và b. 
# Hàm is_prime(n) được sử dụng để kiểm tra xem số n có phải là số nguyên tố hay không. 
# Ta sử dụng hai vòng lặp for để tìm tất cả các cặp số (a,b) thoả mãn 
# điều kiện và có ước chung lớn nhất là số nguyên tố, và sau đó in ra các cặp số đó. 
# Lưu ý rằng, ta chỉ cần kiểm tra các giá trị b lớn hơn a trong vòng lặp for đầu tiên, 
# vì nếu (a,b) thỏa mãn thì (b,a) cũng thỏa mãn.




