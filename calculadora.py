def calculadora():
    print("Calculadora Simple en Python")
    print("Operaciones disponibles:")
    print("1. Suma (+)")
    print("2. Resta (-)")
    print("3. Multiplicación (*)")
    print("4. División (/)")
    print("5. Salir")
    
    while True:
        try:
            opcion = input("\nSeleccione una operación (1-5): ")
            
            # Verificar si el usuario quiere salir
            if opcion == '5':
                print("¡Gracias por usar la calculadora!")
                break
                
            # Validar la opción ingresada
            if opcion not in ['1', '2', '3', '4']:
                print("Error: Opción no válida. Intente nuevamente.")
                continue
                
            # Pedir los números
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            
            # Realizar la operación seleccionada
            if opcion == '1':
                resultado = num1 + num2
                print(f"\n{num1} + {num2} = {resultado}")
            elif opcion == '2':
                resultado = num1 - num2
                print(f"\n{num1} - {num2} = {resultado}")
            elif opcion == '3':
                resultado = num1 * num2
                print(f"\n{num1} * {num2} = {resultado}")
            elif opcion == '4':
                if num2 == 0:
                    print("\nError: No se puede dividir entre cero.")
                else:
                    resultado = num1 / num2
                    print(f"\n{num1} / {num2} = {resultado}")
                    
        except ValueError:
            print("Error: Por favor ingrese números válidos.")
        except Exception as e:
            print(f"Error inesperado: {e}")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculadora()
