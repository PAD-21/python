#bai1 giai pt bac 2
"""
import math
a=float(input("nhap a"))
b=float(input("nhap b"))
c=float(input("nhap c"))

if(a!=0):
    delta = b**2-4*a*c
    if(delta<0):
        print("pt vo nghiem")
    elif (delta==0):
        x=-b/(2*a)
        print("Co nghiem kep x1=x2=: ",x)
    else:
        x1= (-b+math.sqrt(delta))/(2*a)
        x2= (-b-math.sqrt(delta))/(2*a)
        print("Co nghiem x1={0} va x2={1}".format(x1,x2))

else:
    print("khong la pt bac hai")
"""
"""
bai2 Nhap 3 diem tren he truc toa do 
1.xac dinh 3 diem co tao thanh tam giac
2 neu tao thanh tam giac
    - xuat ra chu vi cua tam giac
    - xuat ra dien tich
"""
import math
xA = int(input("nhap xA :"))
yA = int(input("Nha[ yA :"))
xB = int(input("nhap xB :"))
yB = int(input("nhap xB :"))
xC = int(input("nhap xC :"))
yC = int(input("nhap yc :"))

canhAB=math.sqrt((xB-xA)**2+(yB-yA)**2)
canhAC=math.sqrt((xC-xA)**2+(yC-yA)**2)
canhBC=math.sqrt((xC-xB)**2+(yC-yB)**2)

if(canhAB+canhBC > canhAC) and (canhAB+canhAC>canhBC) and (canhAB +canhAC>canhAB):
    print("ABC la tam giac")
    cv =canhAB+canhAC+canhBC
    print("Chu vi = ",cv)

    p=cv/2
    s=math.sqrt(p*(p-canhAB)*(p-canhAC)*(p-canhBC))
    print("dien tich ",s)


else:
    print("ABC khong la tam giac")



