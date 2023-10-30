class sinhvien:
    def __init__(self, hoTen , ngaySinh , que , lop):
        self.hoten = hoTen
        self.ngaySinh = ngaySinh
        self.que = que
        self.lop = lop

    

    def nhapTT():
        hoTen = input("nhập họ tên")
        ngaySinh = input("nhập ngày sinh:")
        que = input("nhập quê")
        lop = input("nhập lớp")
        
    def inTT(self):
        print("hoten: {0} , ngaysinh: {1} , que: {2} , lop: {3}".format(self.hoten,self.ngaySinh,self.que,self.lop))

sv = sinhvien("duy","14/5/2002","Nghệ An","AT17G")
#sv.nhapTT()
sv.inTT()

        