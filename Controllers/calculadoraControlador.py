from colorama import Fore, Style
class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
  
    def ejecutar_c(self):

        while True:
            self.vista.mostrar_menu()
            opcion = input(Fore.LIGHTBLUE_EX + "Seleccione una opcion: " + Style.RESET_ALL)
            if opcion == '1':

                while True:

                    num1, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not num2.strip():
                        self.vista.mostrar_mensaje(Fore.LIGHTRED_EX + "Error: No se Ingreso Algun Parametro." + Style.RESET_ALL)
                    else:

                        try:
                            num1 = int(num1) 
                            try:
                                    num2 = int(num2)
                                    self.modelo.agregar_operacion(num1, "+", num2)
                                    resultado = self.modelo.sumar(num1, num2)
                                    self.modelo.agregar_resultado(resultado)
                                    self.vista.mostrar_mensaje(f"La Suma de {num1} + {num2} Es: {self.modelo.sumar(num1, num2)}")
                                    id_operacion = self.modelo.obtener_id_operaciones()
                                    id_resultado = self.modelo.obtener_id_resultado()
                                    self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                    break
                            except ValueError:
                                self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se permiten numeros" + Style.RESET_ALL)
                            
                        except ValueError:
                            self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se permiten numeros" + Style.RESET_ALL)

            elif opcion == '2':

                while True:

                    num1, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not num2.strip():
                        self.vista.mostrar_mensaje(Fore.GREEN + "Error: No se ingreso algun parametro." + Style.RESET_ALL)
                    else:

                        try:
                            num1 = int(num1)
                            try:
                                num2 = int(num2)
                                self.modelo.agregar_operacion(num1, "-", num2)   
                                resultado = self.modelo.resta(num1, num2)
                                self.modelo.agregar_resultado(resultado)
                                self.vista.mostrar_mensaje(f"La Resta de {num1} - {num2}  Es: {self.modelo.resta(num1, num2)}")
                                id_operacion = self.modelo.obtener_id_operaciones()
                                id_resultado = self.modelo.obtener_id_resultado()
                                self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                break

                            except ValueError:
                                self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se permiten numeros" + Style.RESET_ALL)
                            
                        except ValueError:
                            self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se permiten numeros" + Style.RESET_ALL)

            elif opcion  == '3':

                while True:

                    num1, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not num2.strip():
                        self.vista.mostrar_mensaje(Fore.GREEN + "Error: No se Ingreso Algun Parametro." + Style.RESET_ALL)
                    else:

                        try:
                            num1 = int(num1)

                            try:
                                num2 = int(num2)
                                self.modelo.agregar_operacion(num1 , "*", num2)
                                resultado = self.modelo.multiplicar(num1, num2)
                                self.modelo.agregar_resultado(resultado)
                                self.vista.mostrar_mensaje(f"La Multiplicacion de {num1} x {num2} Es: {self.modelo.multiplicar(num1, num2)}")
                                id_operacion = self.modelo.obtener_id_operaciones()
                                id_resultado = self.modelo.obtener_id_resultado()
                                self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                break

                            except ValueError:
                                self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se Permiten Numeros" + Style.RESET_ALL)
                        
                        except ValueError:
                            self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se Permiten Numeros" + Style.RESET_ALL)

            elif opcion == '4':
                while True:

                    num1, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not num2.strip():
                        self.vista.mostrar_mensaje(Fore.GREEN + "Error: No se ingreso algun parametro." + Style.RESET_ALL)
                    else:

                        try:
                            num1 = int(num1) 

                            if num2 == "0":
                                    self.vista.mostrar_mensaje(Fore.CYAN + "No se puede Dividir entre 0" + Style.RESET_ALL)
                                
                            else:
                                try:
                                    num2 = int(num2)
                                    self.modelo.agregar_operacion(num1, "/", num2)
                                    resultado = self.modelo.dividir(num1, num2)
                                    self.modelo.agregar_resultado(resultado)
                                    self.vista.mostrar_mensaje(f"La Divicion de {num1} / {num2} Es: {self.modelo.dividir(num1, num2)}")
                                    id_operacion = self.modelo.obtener_id_operaciones()
                                    id_resultado = self.modelo.obtener_id_resultado()
                                    self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                    break

                                except ValueError:
                                    self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se Permiten Numeros." + Style.RESET_ALL)
                            
                        except ValueError:
                            self.vista.mostrar_mensaje(Fore.MAGENTA + "Error: Solo se Permiten Numeros." + Style.RESET_ALL)

            elif opcion == '5':
                historial = self.modelo.historial()
                if historial:
                    self.vista.mostrar_historial(historial)
                else:
                    self.vista.mostrar_mensaje(Fore.RED + "No hay Registros en el Historial." + Style.RESET_ALL)
                    break

            elif opcion =='6':
                self.vista.mostar_mensaje("Saliendo de la Calculadora.")
                break
            else:
                self.vista.mostrar_mensaje(Fore.MAGENTA + "Opcion no válida, Intentelo de nuevo." + Style.RESET_ALL)