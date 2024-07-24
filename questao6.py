soma_quinzena1=0
soma_quinzena2=0
list_ip = []
for i in range (1,31):
    ip = int (input("Digite o {}° numero: ".format(i)))
    if i <= 15:
        soma_quinzena1+=ip
    else:
        soma_quinzena2+=ip
    list_ip.append(ip)
    maior = list_ip[0]
    menor = list_ip[0]
    for n in list_ip:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n

for j in range(len(list_ip)):
    if list_ip[j] == maior:
        print(f"O dia que mais choveu foi o {j+1}° dia")
        break 
for k in range(len(list_ip)):
    if list_ip[k] == menor:
        print(f"O dia que menos choveu foi o {k+1}° dia")
        break  
        
print(f"A média pluviométrica da primeira quinzena é {soma_quinzena1/15} %")
print(f"A média pluviométrica da segunda quinzena é {soma_quinzena2/15} %")
