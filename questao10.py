while True:
    peso= float(input("digite seu peso"))
    altura= float(input("digite seu altura"))
    imc= peso/(altura)**2

    if imc < 18.5:
            print("abaixo do peso")

    else:
          if 18.6<imc<24.9:
            print("peso ideal")
            
          else:
            if 24.0<imc<29.9:
                    print("levemente acima do peso")
            else:
                if 30.0<imc<34.9:
                    print("obesidade grau 1")
                else: 
                    if 35.0<imc<39.9:
                        print("obesidade grau 2")
                    else:
                        if imc>=40:
                            print("obesidade grau 3")
    continuar=input("deseja continuar?")
    if continuar == 'nao':
        break
                    
