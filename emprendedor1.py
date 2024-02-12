#instrucciones
print("ATENCIÓN!! Los valores que se ingresen deben estar en pesos chilenos (números enteros)")
print("")

#usuario ingresa valor 1
precio = input('Ingrese el precio de la suscripción en pesos: $ ')
#usuario ingresa valor 2
usuarios = input('Ingrese la cantidad de usuarios de la suscripción: ')
#usuario ingresa valor 3
gastos_totales = input('Ingrese gastos totales en pesos: $ ')

#se calcula el resultado esperado
utilidades = int(precio)*int(usuarios) - int(gastos_totales)

#resultado se imprime en pantalla
print(f"Las utilidades en pesos son: $ {utilidades}")