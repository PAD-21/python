class Ngay:
    #constructor
    def __init__(self,ngay , thang, nam):
        self.ngay = ngay
        self.thang= thang
        self.nam = nam

    #xac dinh so ngay cua thang:
    def soNgayCuaThang(thang,nam):
        if(thang in [1,3,5,7,8,10,12]):
            return 31
        elif(thang in [4,6,9,11]):
            return 30
        elif(thang==2):
            if((nam%400==0 ) or (nam %4==0 and nam%100!=0)):
                return 29
            else:
                return 28
    def ngayTrongNam(self):
        #15/3/2022:
        
        ngayTrongNam=0
        for x in range(1,self.thang):
            ngayTrongNam= ngayTrongNam+Ngay.soNgayCuaThang(x, self.nam)
        ngayTrongNam+=self.ngay
        return ngayTrongNam

ngayA = Ngay(15,3,2022)
print(ngayA.ngayTrongNam())