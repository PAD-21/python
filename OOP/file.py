#open()
#"x" - tao file
"""try:
    f=open("Vidu1.txt","x")
except Exception as e:
    print(e)
finally:
    f.close()
"""
#"w" ghi file
#"a" noi du lieu
"""try:
    with open("vidu1.txt","w") as f:
        f.write("Xin chao cac ban.")
        f.close()
except Exception as e:
    print(e)

try:
    with open("vidu1.txt","a") as f:
        f.write("Xin chao cac ban.")
        f.close()
except Exception as e:
    print(e)
"""
#"r" doc file
try:
    with open("vidu1.txt","r") as f:
        list_noidung = f.readlines()
        i=1
        for noidung in list_noidung:
            print(str(i)+" : " +noidung)
            i+=1
except Exception as e:
    print(e)
