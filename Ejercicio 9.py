inversion = float(input("Total a invertir: "))
interes = float(input("Interes anual: "))
años = int(input("numero dcde años: "))
capital = inversion + interes + años
print ("el capital será de: " + str(round(inversion * (interes / 100 + 1) ** años, 2)))