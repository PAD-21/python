import random
#khai bao set
thungPhieu = set()

#vong lap
while(True):
    print("-------Menu--------")
    print("Vui lòng lựa chọn chức năng: ")
    print("1- Thêm 1 số điện thoại vào thùng")
    print("2- Xóa 1 số điện thoại ")
    print("3- Quay số ngẫu nhiên ")
    print("4- Kết thúc")
    print("Thùng phiếu hiện tai:")
    print(thungPhieu)

    luaChon = int(input("lua chon "))
    if(luaChon ==1):
        soDienThoai = input("Nhap so dt du thuong:")
        thungPhieu.add(soDienThoai)
    elif(luaChon==2):
        sodienThoai=input("Nhap so dt can xoa")
        thungPhieu.discard(soDienThoai)
    elif(luaChon==3):
        index =random.randint(0,len(thungPhieu)-1)
        print("Vị trí trúng thưởng "+str(index))
        i=0
        for x in thungPhieu:
            if(i==index):
                break
            i=i+1
            
        print("Chúc mừng SĐT: "+ x + "đã trúng thưởng")
        thungPhieu.discard(x)
    else:
        break;

    

    
