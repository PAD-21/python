kiemTraSoChan = lambda a:(a%2==0)
print(kiemTraSoChan(6))

tinhTong = lambda a,b:a+b
print(tinhTong(5,10))

def hamMU(n):
    return lambda x:x**n
hamMU2=hamMU(2)
hamMU3=hamMU(3)

print(hamMU2(3))