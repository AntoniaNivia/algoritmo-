while True:
    salario=int(input("digite seu salario:"))
    if salario <= 1500:
        irpf=salario*0.05
        salario_liquido=salario-irpf
        print(irpf)
        print(salario)
        print(salario_liquido)
    else:
        if salario>1500 and salario<3000:
            irpf=salario*0.08
            salario_liquido=salario-irpf
            print(irpf)
            print(salario)
            print(salario_liquido)
        else:
            if salario>3000 and salario<10000:
                irpf=salario*0.15
                salario_liquido=salario-irpf
                print(irpf)
                print(salario)
                print(salario_liquido)
            else:
                if salario>15000:
                    irpf=salario*0.27
                    salario_liquido=salario-irpf
                print(irpf)
                print(salario)
                print(salario_liquido)
    continuar=input("deseja continuar?")
    if continuar == 'nao':
        break

