import mysql.connector

class ModeloCaculadora:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database= "calcu"
            )
            self.cursor = self.con.cursor()
        except mysql.connector.Error as e:
            print(f"Error de conexión a la base de datos: {e}")

    def historial(self):
        try:
            self.cursor.execute(""" SELECT o.id, o.num1 AS Primer_Numero, op.operador AS Signo, o.num2 AS segundo_Numero , o.resultado
            FROM operacion AS o
            JOIN operadores AS op ON o.id = op.id 
            ORDER BY o.id DESC 
            """)            
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error Al ver el Historial: {e}")
        
    def agregar_operacion(self, num1, id_operador, num2, resultado):  #agrega los datos ingresados de las operaciones 
        try:
            consulta = "INSERT INTO operacion (num1, id_operador, num2, resultado) VALUES (%s, %s, %s, %s)"
            self.cursor.execute(consulta, (num1, id_operador, num2, resultado))
            self.con.commit()
        except mysql.connector.Error as e:
            print(f"Error Al agregar la Operación : {e}")

  
    def sumar(self, num1, num2):  #funcion suma
        return num1 + num2
    
    def resta(self, num1, num2): #funcion resta
        return num1 - num2
    
    def multiplicar(self, num1,num2):  #funcion multiplicacion
        return num1 * num2
    
    def dividir(self, num1, num2):  # funcion divicion 
        return num1 / num2


