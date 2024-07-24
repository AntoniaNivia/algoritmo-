I= float(input("digite uma nota:"))
II= float(input("digite uma nota:"))
III= float(input("digite uma nota:"))
IV= float(input("digite uma nota:"))
V= float(input("digite uma nota:"))

if I >=7 and II >=7 and III >=7 and IV >=7 and V>=7:
    print("A-passou em todos os exames")

elif I>=7 and II>=7 and IV>=7 and (III<7 or V<7):
    print("B-passou em I, II e IV")

elif I>=7 and II>=7 and (III>=7 or IV>=7) and V<7:
    print("C-passou em I, II, III ou IV")

else:
    print("reprovado")