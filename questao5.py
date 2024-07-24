A= 5000000
B= 7000000
c = 0
while A<B:
    A= A+A*0.03
    B= B+B*0.02
    c+=1
print(" o tempo necessário para que a população do país A ultrapasse a população do país B: ", c)