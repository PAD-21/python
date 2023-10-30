#tao list rong
emptyList = []
#Tao ra mot doi tuong list
emptyList2 = list()

print(emptyList)
print(emptyList2)

# tao ra list co du lieu
colors =["red" , "green" ,"orange" ]
print(colors)

#list co thu tu , vi tri cac phtu duoc danh dau tu 0 ,tu trai sang phai
ListSV = ["Duy", "thang", "Bich"]
print(ListSV[2])

print(ListSV[1:2])

#them phtu vao list
#them vao cuoi
ListSV.append("Vinh")
print(ListSV)
ListSV[len(ListSV):] = ["chuot"]

ListSV.insert(2,"Trang")
print(ListSV)

#so luong phtu co trong list : len
print(len(ListSV))

#dem so luong phtu thoa dieu kien
print("dem duy: ", ListSV.count("duy"))

#kiem tra phtu co ben trong list:in
if("chuot" in ListSV):
#xoa phtu
    ListSV.remove("chuot")
    print(ListSV)

#xoa phtu ra hhoi list bang vi tri
ListSV.pop(1)
print(ListSV)

#dao nguoc list
ListSV.reverse()
print(ListSV)

#sap xep 
ListSV.sort()
print(ListSV)

number = [ 1, 4,5,2,8]
number.sort()
print(number)

#sap xep nguoc
ListSV.sort(reverse=True)
print(ListSV)

number.sort(reverse=True)
print(number)

#xoa sach du lieu trong list
ListSV.clear()
print(ListSV)
