from colorama import Fore, Style
from Models.calculadoraModelo import ModeloCaculadora
from Views.calculadoraVista import VistaCalculador
from Controllers.calculadoraControlador import ControladorCalculadora


if __name__ == "__main__":     

    modelo_calculadora = ModeloCaculadora()
    vista_calculadora = VistaCalculador()
    controlador_calculadora = ControladorCalculadora(modelo_calculadora, vista_calculadora) 

while True:  #menu principal
    print(Fore.LIGHTGREEN_EX +"\n--- Sistema Calculadora ---" + Style.RESET_ALL)
    print("1. Calculadora")
    print("2. Salir")
    opcion = input(Fore.LIGHTBLUE_EX + "Seleccione una opción (1-2): " + Style.RESET_ALL)

    if opcion == '1':  # Calculadora
        controlador_calculadora.ejecutar_c()
    elif opcion == '2': # Salir
        print(Fore.MAGENTA + "Saliendo de la Calculadora." + Style.RESET_ALL )
        break
    else:
        print(Fore.MAGENTA + "Opción no valída."+ Style.RESET_ALL)
        