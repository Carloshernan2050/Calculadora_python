from Models.Modelo import ModeloCaculadora
from Views.calculadoraVista import VistaCalculador
from Controllers.calculadoraControlador import ControladorCalculadora


if __name__ == "__main__":     

    modelo_calculadora = ModeloCaculadora()
    vista_calculadora = VistaCalculador()
    controlador_calculadora = ControladorCalculadora(modelo_calculadora, vista_calculadora) 

while True:
    print("\n--- Sistema Calculadora ---")
    print("1. Calculadora")
    print("2. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':  # Calculadora
        controlador_calculadora.ejecutar_c()
    elif opcion == '2': # Salir
        print("Saliendo de la Calculadora.")
        break
    else:
        print("Opcion no valida.")
        