import mysql.connector

class ModeloCaculadora:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database= "calculadora"
            )
            self.cursor = self.con.cursor()
        except mysql.connector.Error as e:
            print(f"Error de conexión a la base de datos: {e}")

        
    def agregar_al_historial(self, id_operacion, id_resultado): #agrega las operaciones generadas al historial
        try:
            consulta = "INSERT INTO operacion_resultado (id_operacion, id_resultado) VALUES (%s, %s)"
            self.cursor.execute(consulta, (id_operacion, id_resultado))
            self.con.commit()
        except mysql.connector.Error as e:
            print(f"Error Al agregar al historial: {e}")

    def historial(self):
        try:
            self.cursor.execute("""SELECT op.id, o.num1 AS Primer_Numero, o.operador AS Signo, o.num2 AS segundo_Numero , r.resultados
            FROM operacion_resultado AS op
            JOIN operacion AS o ON op.id = o.id
            JOIN resultado AS r ON op.id = r.id
            GROUP BY o.id
            ORDER BY op.id DESC                 
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error Al ver el Historial: {e}")
        
    def agregar_operacion(self, num1, operador, num2):  #agrega los datos ingresados de las operaciones 
        try:
            consulta = "INSERT INTO operacion (num1, operador, num2) VALUES (%s, %s, %s)"
            self.cursor.execute(consulta, (num1, operador, num2))
            self.con.commit()
        except mysql.connector.Error as e:
            print(f"Error Al agregar la Operacion : {e}")

    def agregar_resultado(self, resultados): #agrega los resultados de las operaciones 
        try:
            consulta = "INSERT INTO resultado (resultados) VALUES (%s)"
            self.cursor.execute(consulta,(resultados,))
            self.con.commit()
        except mysql.connector.Error as e:
            print(f"Error Al agregar el Resultado: {e}")
    
    def obtener_id_operaciones(self):  #muestra el id de las operaciones

        try:
            consulta = "SELECT id FROM operacion ORDER BY id DESC LIMIT 1"
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchone()
            return resultado[0]
           
        except mysql.connector.Error as e:
            print(f"Error Al obtener el id de la operacion: {e}")
        
    def obtener_id_resultado(self):#muestra el id del resultado

        try:
            consulta = "SELECT id FROM resultado ORDER BY id DESC LIMIT 1"
            self.cursor.execute(consulta)
            resultado = self.cursor.fetchone()
            return resultado[0]
            
        except mysql.connector.Error as e:
            print(f"Error Al obtener elid de reultados: {e}")
        
    def sumar(self, num1, num2):  #funcion suma
        return num1 + num2
    
    def resta(self, num1, num2): #funcion resta
        return num1 - num2
    
    def multiplicar(self, num1,num2):  #funcion multiplicacion
        return num1 * num2
    
    def dividir(self, num1, num2):  # funcion divicion 
        return num1 / num2


