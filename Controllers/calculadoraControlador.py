class ControladorCalculadora:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

    
    def ejecutar_c(self):

        while True:
            self.vista.mostrar_menu()
            opcion = input("Seleccione una opcion: ")

            if opcion == '1':

                while True:

                    num1, operador, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not operador.strip() or not num2.strip():
                        self.vista.mostrar_mensaje("Error: No se Ingreso Algun Parametro.")
                    else:

                        try:
                            num1 = int(num1) 

                            if  operador != "+":
                                self.vista.mostrar_mensaje("Error: De acuerdo con la 0peracion eligida el Signo debe ser + ")


                            else:
                                try:
                                    num2 = int(num2)
                                    self.modelo.agregar_operacion(num1, operador, num2)
                                    resultado = self.modelo.sumar(num1, num2)
                                    self.modelo.agregar_resultado(resultado)
                                    self.vista.mostrar_mensaje(f"La Suma de {num1} + {num2} Es: {self.modelo.sumar(num1, num2)}")
                                    id_operacion = self.modelo.obtener_id_operaciones()
                                    id_resultado = self.modelo.obtener_id_resultado()
                                    self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                    break
                                except ValueError:
                                    self.vista.mostrar_mensaje("Error: Solo se permiten numeros")
                            
                        except ValueError:
                            self.vista.mostrar_mensaje("Error: Solo se permiten numeros")

            


            elif opcion == '2':

                while True:

                    num1, operador, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not operador.strip() or not num2.strip():
                        self.vista.mostrar_mensaje("Error: No se ingreso algun parametro.")
                    else:

                        try:
                            num1 = int(num1)

                            if  operador != "-":
                                self.vista.mostrar_mensaje("Error: De acuerdo con la 0peracion eligida el Signo debe ser -")

                            else:
                                try:
                                    num2 = int(num2)
                                    self.modelo.agregar_operacion(num1, operador, num2)   
                                    resultado = self.modelo.resta(num1, num2)
                                    self.modelo.agregar_resultado(resultado)
                                    self.vista.mostrar_mensaje(f"La Resta de {num1} - {num2}  Es: {self.modelo.resta(num1, num2)}")
                                    id_operacion = self.modelo.obtener_id_operaciones()
                                    id_resultado = self.modelo.obtener_id_resultado()
                                    self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                    break

                                except ValueError:
                                    self.vista.mostrar_mensaje("Error: Solo se permiten numeros")
                            
                        except ValueError:
                            self.vista.mostrar_mensaje("Error: Solo se permiten numeros")


            elif opcion  == '3':

                while True:

                    num1, operador, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not operador.strip() or not num2.strip():
                        self.vista.mostrar_mensaje("Error: No se Ingreso Algun Parametro.")
                    else:

                        try:
                            num1 = int(num1)

                            if  operador != "*":
                                self.vista.mostrar_mensaje("Error: De acuerdo con la 0peracion eligida el Signo debe ser *")

                            else:
                                try:
                                    num2 = int(num2)
                                    self.modelo.agregar_operacion(num1 , operador, num2)
                                    resultado = self.modelo.multiplicar(num1, num2)
                                    self.modelo.agregar_resultado(resultado)
                                    self.vista.mostrar_mensaje(f"La Multiplicacion de {num1} x {num2} Es: {self.modelo.multiplicar(num1, num2)}")
                                    id_operacion = self.modelo.obtener_id_operaciones()
                                    id_resultado = self.modelo.obtener_id_resultado()
                                    self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                    break

                                except ValueError:
                                    self.vista.mostrar_mensaje("Error: Solo se Permiten Numeros")
                            
                        except ValueError:
                            self.vista.mostrar_mensaje("Error: Solo se Permiten Numeros")


            elif opcion == '4':
                while True:

                    num1, operador, num2 = self.vista.obtener_datos_operacion()
                    if not num1.strip() or not operador.strip() or not num2.strip():
                        self.vista.mostrar_mensaje("Error: No se ingreso algun parametro.")
                    else:

                        try:
                            num1 = int(num1) 

                            if  operador != "/":
                                self.vista.mostrar_mensaje("Error: De acuerdo con la 0peracion eligida el Signo debe ser +")

                            else:
                                if num2 == "0":
                                    self.vista.mostrar_mensaje("No se puede Dividir entre 0")
                                
                                else:
                                    try:
                                        num2 = int(num2)
                                        self.modelo.agregar_operacion(num1, operador, num2)
                                        resultado = self.modelo.dividir(num1, num2)
                                        self.modelo.agregar_resultado(resultado)
                                        self.vista.mostrar_mensaje(f"La Divicion de {num1} / {num2} Es: {self.modelo.dividir(num1, num2)}")
                                        id_operacion = self.modelo.obtener_id_operaciones()
                                        id_resultado = self.modelo.obtener_id_resultado()
                                        self.modelo.agregar_al_historial(id_operacion, id_resultado)
                                        break

                                    except ValueError:
                                        self.vista.mostrar_mensaje("Error: Solo se Permiten Numeros")
                            
                        except ValueError:
                            self.vista.mostrar_mensaje("Error: Solo se Permiten Numeros")
                


            elif opcion == '5':
                historial = self.modelo.historial()
                self.vista.mostrar_historial(historial)


            elif opcion =='6':
                self.vista.mostar_mensaje("Saliendo de la Calculadora.")
                break
            else:
                self.vista.mostrar_mensaje("Opcion no válida, Intentelo de nuevo")