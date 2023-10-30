gioiTinh = ("Nam","Nữ")
lopHoc=(1,2,3,4,5,6,7,8)
traiCay=("Táo","Chuối","Táo","Cam")

print(gioiTinh[0])
print(traiCay[0:2])

for x in traiCay:
    print(x)

y=(1,2,3)+(4,5,6)
print(y)

print("Táo" in traiCay)
#lay so luong ptu
x=len(traiCay)
print(x)
#dem so luong
print(traiCay.count("Táo"))

print(sum(lopHoc))

listTC = sorted(traiCay)
print(listTC)