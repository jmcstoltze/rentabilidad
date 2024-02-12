#instrucciones
print("ATENCIÓN!! Los valores que se ingresen deben estar en pesos chilenos (números enteros)")
print("")

#usuario ingresa valor 1
precio = input('Ingrese el precio de la suscripción en pesos: $ ')
#usuario ingresa valor 2
usuarios = input('Ingrese la cantidad de usuarios de la suscripción: ')
#usuario ingresa valor 3
gastos_totales = input('Ingrese gastos totales en pesos: $ ')

#usuario ingresa valor 4
utilidades_anterior = input('Ingrese utilidades año anterior en pesos: $ ')

#se calcula el resultado 1 esperado (utilidades)
utilidades = int(precio)*int(usuarios) - int(gastos_totales)

#se calcula el resultado 2 esperado (razón entre las utilidades utilidades) con 2 decimales
razon = round(utilidades/int(utilidades_anterior),2)

#resultado 1 se imprime en pantalla
print(f"Las utilidades para este año en pesos son: $ {utilidades}")

#resultado 2 se imprime en pantalla
print(f"La razón entre las utilidades de este año y el anterior es de: {razon}")