from colorama import Fore, Style
class VistaCalculador:

    @staticmethod
    def mostrar_menu():
        print(Fore.LIGHTWHITE_EX + "\n--- Caculadora ---" + Style.RESET_ALL )
        print(Fore.GREEN + "1. Sumar" + Style.RESET_ALL)
        print(Fore.GREEN +"2. Restar" + Style.RESET_ALL)
        print(Fore.CYAN+ "3. Multiplicar" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Dividir" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Historial" + Style.RESET_ALL)
        print(Fore.RESET + "6. Salir" + Style.RESET_ALL)
    
    @staticmethod
    def obtener_datos_operacion():
        num1 = input(Fore.CYAN + "Ingrese El Primer Numero: \n" + Style.RESET_ALL) 
        num2 = input(Fore.CYAN + "Ingrese El Segundo Numero: \n" + Style.RESET_ALL)
        return num1, num2

    @staticmethod
    def mostrar_historial(historial):
        print(Fore.CYAN + "\n--- Historial de Operaciones ---" + Style.RESET_ALL)
        for operacion in historial:
            print(f"ID: {operacion[0]}, Primer Numero : {operacion[1]} Signo: {operacion[2]}, Segundo Numero: {operacion[3]}, Resultado: {operacion[4]}")
           
    @staticmethod
    def mostrar_mensaje(mensaje):
        print(f"\n{mensaje}")
    