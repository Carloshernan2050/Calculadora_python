from colorama import Fore, Style
from Models.calculadoraModelo import ModeloCaculadora
from Views.calculadoraVista import VistaCalculador
from Controllers.calculadoraControlador import ControladorCalculadora


if __name__ == "__main__":     

    modelo_calculadora = ModeloCaculadora()
    vista_calculadora = VistaCalculador()
    controlador_calculadora = ControladorCalculadora(modelo_calculadora, vista_calculadora) 

while True:
    print(Fore.LIGHTGREEN_EX +"\n--- Sistema Calculadora ---" + Style.RESET_ALL)
    print("1. Calculadora")
    print("2. Salir")
    opcion = input(Fore.LIGHTRED_EX + "Seleccione una opción: " + Style.RESET_ALL)

    if opcion == '1':  # Calculadora
        controlador_calculadora.ejecutar_c()
    elif opcion == '2': # Salir
        print("Saliendo de la Calculadora.")
        break
    else:
        print("Opcion no valida.")
        