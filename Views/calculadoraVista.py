class VistaCalculador:

    @staticmethod
    def mostrar_menu():
        print("\n--- Caculadora ---")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Historial")
        print("6. Salir")
    
    @staticmethod
    def obtener_datos_operacion():
        num1 = input("Ingrese el primer numero: ")
        print()
        print( "Signos Disponibles [+, -, *, /]" )
        print()
        operador = input("Ingrese el signo de la operacion : ")
        print()
        num2 = input("Ingrese el segundo numero:")
        return num1, operador, num2
    
    @staticmethod
    def mostrar_historial(historial):
        print("\n--- Historial de Operaciones ---")
        for operacion in historial:
            print(f"ID: {operacion[0]}, Primer Numero : {operacion[1]} Signo: {operacion[2]}, Segundo Numero: {operacion[3]}, Resultado: {operacion[4]}")
           

    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"\n{mensaje}")