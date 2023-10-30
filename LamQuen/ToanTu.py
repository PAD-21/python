x=int(input("x:"))
y= int (input("y:"))

#so sanh
print("{0}<{1} la {2}".format(x,y,x<y))
print("{0}>{1} la {2}".format(x,y,x>y))
print("{0}=={1} la {2}".format(x,y,x==y))
print("{0}!={1} la {2}".format(x,y,x!=y))
print("{0}>={1} la {2}".format(x,y,x>=y))
print("{0}<={1} la {2}".format(x,y,x<=y))

#logic
z=int(input("z:"))
print((x<y) and (y<z))
print((x<y) or (y<z))
print(not(x>z))
