#instrucciones
print("ATENCIÓN!! Los valores monetarios a ingresar deben ser numéricos")
print("")

#usuario ingresa valor suscripción
precio_normal = input('Ingrese el precio de la suscripción para usuarios normales en pesos: $ ')

#se calcula el valor suscripción usuario premium (sumándole 50%) y se imprime en pantalla
precio_premium = int(precio_normal)*1.5
print(f"La suscripción para usuarios premium será de: $ {precio_premium}")

#usuario ingresa cantidad 1
usuarios_normales = input('Ingrese la cantidad de usuarios normales: ')
#usuario ingresa cantidad 2 
usuarios_premium = input('Ingrese la cantidad de usuarios premium: ')

#usuario ingresa gastos totales
gastos_totales = input('Ingrese gastos totales en pesos: $ ')

#se calcula el resultado esperado redondeando 2 decimales
utilidades = round((float(precio_normal)*float(usuarios_normales)) + (float(precio_premium)*float(usuarios_premium)) - float(gastos_totales),2)

#resultado se imprime en pantalla
print(f"Las utilidades en pesos son: $ {utilidades}")