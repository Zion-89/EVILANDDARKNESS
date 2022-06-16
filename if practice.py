edad = 18
sexo = "masculino"
permitido = False

if edad >=18:
    permitido=True
    print(permitido)
else:
    print("vaya lavese las nachas joven")
    print(permitido)

if edad>=18:#este criterio se cumplio
    permitido=True
    if sexo=="femenino":
        print("No tiene costo mi reina")
    else:#se utiliza por tener criterio negativo o falso
        print("son 2000 pesitos papu")
print(permitido)