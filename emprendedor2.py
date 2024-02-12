#instrucciones
print("ATENCIÓN!! Los valores que se ingresen deben estar en pesos chilenos (números enteros)")
print("")

#usuario ingresa valor suscripción
precio_normal = input('Ingrese el precio de la suscripción para usuarios normales en pesos: $ ')

#se calcula el valor suscripción usuario premium y se imprime en pantalla
precio_premium = int(precio_normal)*2
print(f"La suscripción para usuarios premium será de: $ {precio_premium}")

#usuario ingresa cantidad 1
usuarios_normales = input('Ingrese la cantidad de usuarios normales: ')
#usuario ingresa cantidad 2 
usuarios_premium = input('Ingrese la cantidad de usuarios premium: ')

#usuario ingresa gastos totales
gastos_totales = input('Ingrese gastos totales en pesos: $ ')

#se calcula el resultado esperado
utilidades = (int(precio_normal)*int(usuarios_normales)) + (int(precio_premium)*int(usuarios_premium)) - int(gastos_totales)

#resultado se imprime en pantalla
print(f"Las utilidades en pesos son: $ {utilidades}")