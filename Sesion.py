#Esta es una libreria la utilice en el avance1 tambien explico el porque 
import matplotlib.pyplot as plt

#Todos los Pacientes "TIENEN UN"
class Sesion:
    def __init__(self, puntos, tiempo_de_captura):
        self.puntos = puntos
        self.tiempo_de_captura = tiempo_de_captura
        #¿Porque tengo un apartado de creacion de una lista vacia?
        #Podria hacer exactamente lo mismo con el apartado de puntos y poder promediar su resulatado 
        #Pero la idea de este programa es que el usuario puede o no realizar prueba de sangre 
        #Y el programa puede funcionar mas adelante explico las condiciones 
        self.pruebas_sangre = []

    def resultados_de_prueba(self):
        #simpplemente la funcion que "TIENE UN" paciente pero tambien se lo puedo hacer a un perro 
        print(f"Consiguió un puntaje de: {self.puntos}")
        print(f"Tardó: {self.tiempo_de_captura} s")

    def contador_de_puntos(self):
        #Esta es otra funcion que nos permite evaluar los puntos, el usuario puede acceder a ella o no 
        #En la funcion del paciente la mostramos pero podriamos perfectamente omitirla si es que 
        #Le pongo una condicion que le muestre los valores 
        if self.puntos <= 5:
            print("El paciente no logró hacer los ejercicios con eficacia")
        elif 6 <= self.puntos <= 10:
            print("El paciente va por buen camino")
        else:
            print("El paciente ta fuerte")


    #Esta dos funcion son el distintivo de nuestro programa, pues como vemos en la parte de 
    #arriba dejamos una lista sin datos, y pues eso de que nos sirve, pues porque vamos tener en un apartado que
    #Que nos permita ver su valor de sangre sin afectar el resto del programa  
    def agregar_prueba_sangre(self, fecha, glucosa, amh):
        self.pruebas_sangre.append([fecha, glucosa, amh])
    #Este es parte de un programa del avance1 hay explico como funciona todo el programa
    def mostrar_analisis_sangre(self):
        if not self.pruebas_sangre:
            print("En esta sesión no se realizó prueba de sangre")
            return

        lista1 = []
        lista2 = []

        for registro in self.pruebas_sangre:
            fecha, glucosa, amh = registro
            print(f"Registro -> Fecha: {fecha} | Glucosa: {glucosa} | AMH: {amh}")

            glucosa = int(glucosa)
            amh = int(amh)

            lista1.append(glucosa)
            lista2.append(amh)

            # Evaluación de estado
            if glucosa > 120 and amh < 80:
                print(" -> El paciente en esta fecha tuvo estrés")
            elif glucosa > 120 and amh > 80:
                print(" -> El paciente se estaba muriendo")
            elif glucosa > 80 and amh < 120:
                print(" -> El paciente tenía muchas hormonas")
            else:
                print(" -> Todo bien con el paciente")

        # Generar gráfica de la sesión
        plt.scatter(lista1, lista2, color="blue")
        plt.xlabel("Glucosa")
        plt.ylabel("AMH")
        plt.title("Pruebas de Sangre de la Sesión")
        plt.grid(True)
        plt.show()


class Paciente:
#Y pues todo esto pues es el paciente, todos los paciente tienen una sesion, pero no son una sesion 
#Este pues es chiquito ni para que lo explico, lo unico que se va a explicar es la parte de la sesion, que 
#si bien sesion puede tomar valores como 1 al momento de crear el objeto los vamos a definir apartir 
#de la clase sesion, es mas facil desde el archivo main.py
    def __init__(self, Nombre, Edad, Estatura, sesion=None):
        self.nombre = Nombre
        self.Edad = Edad
        self.Estatura = Estatura
        self.sesion = sesion

    def info(self):
        print(f"\n--- Paciente: {self.nombre} ---")
        print(f"Edad: {self.Edad} | Estatura: {self.Estatura}")
        if self.sesion is not None:
            print("\n[Resultados Físicos]")
            self.sesion.resultados_de_prueba()
            self.sesion.contador_de_puntos()
            print("\n[Pruebas de Sangre]")
            self.sesion.mostrar_analisis_sangre()
        else:
            print("El paciente no tiene ninguna sesión registrada")

