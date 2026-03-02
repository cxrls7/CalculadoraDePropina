print("=== CALCULADORA DE PROPINA ===")
print()


nombre = input("- Ingrese su nombre: ")
print() 
print("- Hola", nombre)
print()


while True:
    try:
        cuenta = float(input("Ingrese el valor de la cuenta: "))
        if cuenta < 0:
            print("- El valor no puede ser negativo. Intente nuevamente.")
        else:
            break 
    except ValueError:
        print("- Entrada inválida. Debe ingresar un número.")


if cuenta < 20:
    porcentaje = 10
elif cuenta <= 50:
    porcentaje = 15
else:
    porcentaje = 20

propina = cuenta * porcentaje / 100
total = cuenta + propina

print("\n----- RESULTADOS -----")
print()
print("- Cuenta: $", cuenta)
print("- Porcentaje aplicado:", porcentaje, "%")
print("- Propina: $", propina)
print("- Total a pagar: $", total)
print()

print("Gracias por usar la calculadora de propina, ¡que tenga un buen día!") 
print()



input("Presione Enter para salir...")


