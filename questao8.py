
a = [[i+j for j in range(4)]for i in range(4)]
b=[]

for i in range(4):
    for j in range(4):
        if i==j:
          dp = a[i][j]
          b.append(dp)

for linha in a:
    print(linha)

print("Essa é a diagonal principal",b)