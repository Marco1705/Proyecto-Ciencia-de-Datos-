import pandas as pd
import matplotlib.pyplot as plt


##Cargar archivo.csv
base_datos = pd.read_csv('Base Datos buena1.1.csv')

is_mex = base_datos["Pais_Name"] == "Mexico"

mexico = base_datos[is_mex]

## Aqui sacamos Minimo, Maximo, Media Y varianza de la canasta basica rural, urbana y del salario minimo

todo = {"Valor": ["Minimo","Maximo","Media","Varianza"],
        "Salario Minimo":[mexico.Salario_minimo.min(),mexico.Salario_minimo.max(),mexico.Salario_minimo.mean(),mexico.Salario_minimo.var()],
        "Canasta basica rural":[mexico.Precio_canasta_basica_rural.min(),mexico.Precio_canasta_basica_rural.max(),mexico.Precio_canasta_basica_rural.mean(),mexico.Precio_canasta_basica_rural.var()],
        "Canasta basica urbana":[mexico.precio_canasta_basica_urbana.min(),mexico.precio_canasta_basica_urbana.max(),mexico.precio_canasta_basica_urbana.mean(),mexico.precio_canasta_basica_urbana.var()]}

todo = pd.DataFrame(todo)
print(todo)

##Quitando los gastos de la canasta basica cuanto dinero sobra para otras necesidades

print("\nSalario minimo diario por un mes restandole canasta basica urbana 1990")
sal = 11.9*30
Res = sal-147.38
print(Res)

print("\nSalario minimo diario por un mes restandole canasta basica urbana 1995")
sal1 = 16.63*30
Res1 = sal1-203.09
print(Res1)

print("\nSalario minimo diario por un mes restandole canasta basica urbana 2000")
sal2 = 37.9*30
Res2 = sal2-381.04
print(Res2)

print("\nSalario minimo diario por un mes restandole canasta basica urbana 2005")
sal3 = 46.8*30
Res3 = sal3-492.66
print(Res3)

print("\nSalario minimo diario por un mes restandole canasta basica urbana 2010")
sal4 = 57.46*30
Res4 = sal4-997.94
print(Res4)

print("\nSalario minimo diario por un mes restandole canasta basica urbana 2016")
sal5 = 73.04*30
Res5 = sal5-1333.7
print(Res5)

