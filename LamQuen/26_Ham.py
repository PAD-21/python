"""def xinChao():
    print("Xin chào")

xinChao()

#đối số được đặt trong cặp ngoặc()
def xinChao(hovaten):
    print("Xinchao: "+hovaten)

xinChao("Anh Duy")

#Nhiều đối số, mỗi đối số cách nhau bởi dấu phẩy
def xinChao(ho,dem,ten):
    print("Xin chao ban: "+ ho + dem + ten)
    print("Xin chao: "+ho)
xinChao("Phan","Anh","Duy")

#khi không xác định được đối số , chúng ta có thể sử dụng dấu *
def thoiKhoaBieu(*monHoc):
    print("Môn 1: " + monHoc[0])
    print("Môn 1: " + monHoc[1])

thoiKhoaBieu("Toán" , "Lý" , "Hóa")

def tinhTong(*giaTri):
    sum=0
    for x in giaTri:
        sum = sum+x
    print("sum = ",+sum)

tinhTong(1,2)
tinhTong(1,5,6,7,8)

#truyền nhiều đối số, xác định thông qua tên
def xinChao(**ten):
    print("Xin chao:"+ten["ho"])

xinChao(ten="Duy",dem="Anh",ho="Phan")

#sử dụng từ khóa return
def tinhTich(*giaTri):
    tich=1
    for x in giaTri:
        tich=tich*x

    return tich
tich1=tinhTich(1,4,6)
print(tich1)
"""
#bai tap:tìm USCLN của hai số tự nhiên a,b
def gcd(a,b):
    while(a!=b):
        if(a>b):
            a=a-b
        else:
            b=b-a
    return a

print(gcd(55,100))

#2: Nhập vào một dãy n số từ bàn phím , viết hàm tính tổng
list_number = []
n=1
while(True):
    try:
        n=int(input("Nhap so luong phtu"))
    except:
        print("Vui lòng nhập n>1")
    if(n>=1):
        break
def nhap(n,list_number):
    for i in range(n):
        list_number.append(int(input("Nhập  giá trị thứ "+str(i)+" : ")))

def tinhTong(list_number):
    tong =0 
    for x in list_number:
        tong=tong+x
    return tong

nhap(n,list_number)
print("Tong = " +str(tinhTong(list_number)))
