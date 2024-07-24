p= 0
s= 1

for cont in range (1,10+1):
    proximo= p + s
    p= s
    s = proximo
    f=1
    if p %2!=0: 
        for i in range (1,p+1):
            f*=i
        print(f)

print("fim")