saldo_medio= int(input("digite seu saldo medio:"))

if saldo_medio<=200:
    credito= 0
    print(saldo_medio)
    print(credito)
    print(saldo_medio+credito)
    
elif saldo_medio<=400:
    credito= 0.20*saldo_medio
    print(saldo_medio)
    print(credito)
    print(saldo_medio+credito)
    
elif saldo_medio<=600:
    credito= 0.30*saldo_medio
    print(saldo_medio)
    print(credito)
    print(saldo_medio+credito)

elif saldo_medio>=601:
    credito= 0.40*saldo_medio
    print(saldo_medio)
    print(credito)
    print(saldo_medio+credito)