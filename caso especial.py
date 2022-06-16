def calculadora(opcion,num1,num2):
    try:
        opcion=int(opcion)
        num1=int(num1)
        num2=int(num2)
        match opcion:
            case 1:
                return num1+num2
            case 2:
                return num1-num2
            case 3: 
                return num1*num2
            case 4:
                return num1/num2
            case default:
                #print("No sea inutil y ingrese bien la vara")
                return"Error"
    except ZeroDivisionError:
        print("Vea mae no se puede dividir por 0, si fue a la escuela?")
        calculadora(opcion,num1,input("Ponga un segundo numero, que no sea 0 caballo"))
    except:
        print("Ya se paseo en esta vara por bestia")


print(calculadora(
    int(input("1.Suma, 2.Resta, 3.Multiplicacion, 4.Division")),
    int(input("Ingrese numero 1")),
    int(input("Ingrese numero 2"))
))