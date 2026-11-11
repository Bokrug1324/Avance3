from Sesion import Sesion,Paciente

sesionpaciente1 = Sesion(puntos=8, tiempo_de_captura=45)
sesionpaciente2 = Sesion(puntos=8, tiempo_de_captura=45)
# 2. Agregar las pruebas a la sesión solo del paciente 1 mas adelante se crea el objeto o paciente
sesionpaciente1.agregar_prueba_sangre("2026-03-01", 130, 70)
sesionpaciente1.agregar_prueba_sangre("2026-04-10", 90, 100)

# 3. Asignar la sesión al paciente observemos que el segundo pasiente funciona
# sin necesidad de pasar por la prubeba de sangre 
paciente1 = Paciente("Santiago", 21, 1.80, sesionpaciente1)
paciente2 = Paciente("Diego", 21, 1.80, sesionpaciente2)
# 4. Ver toda la información
paciente1.info()
paciente2.info()