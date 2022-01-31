altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en kilogramos: "))
imc = round((peso)/(altura)**2,2)
print("Tu indice de masa corporal es: ", str(imc))