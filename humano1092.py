print("Actividad 9 clase humano")
print("Alondra Ramirez Sandoval Mat: 22308051281092")
# Zona de clases 
class Humano1092:
    # zona de atributos dentro de la clase
    edad=0
    fechaN=0
    pais=0
    estatura=0
    idioma=0
    colorc=0


    # zona de funciones dentro de la clase
    def correr1092(self,n):
        print(f"{n} esta corriendo ufff....")
    def cantar1092(self,m):
        print(f"{m} esta cantando The Astronaut")
    def bailar1092(self,j):
        print(f"{j} esta bailando Fake Love") 
    def escuchar1092(self,i):
        print(f"{i} esta escuchando Moon") 
    def accion1092(self,s):
        print(f"{s} esta en un desfile de modas")              

# zona de creacion de objetos
alondra=Humano1092()
seokjin=Humano1092()
# zona de usando objetos
print("----Resultados para Alondra----")
alondra.edad=17
alondra.fechaN="12 de enero 2007"
alondra.pais="Mexico"
alondra.estatura= 1.64
alondra.idioma="español"
print(f"Edad: {alondra.edad}")
print(f"Fecha de Nacimiento: {alondra.fechaN}")
print(f"Pais de Nacimiento: {alondra.pais}")
print(f"Estatura: {alondra.estatura}")
print(f"Idioma nativo: {alondra.idioma}")
print("-----Funciones para Alondra-----")
alondra.correr1092("Alondra")
alondra.cantar1092("Alondra")
alondra.bailar1092("Alondra")
alondra.escuchar1092("Alondra")

print("----Resultados para Seokjin----")
seokjin.edad=31
seokjin.fechaN="04 de diciembre 1992"
seokjin.pais="Corea del sur"
seokjin.estatura= 1.79
seokjin.idioma="coreano"
seokjin.colorc="negro"
print(f"Edad: {seokjin.edad}")
print(f"Fecha de Nacimiento: {seokjin.fechaN}")
print(f"Pais de Nacimiento: {seokjin.pais}")
print(f"Estatura: {seokjin.estatura}")
print(f"Idioma nativo: {seokjin.idioma}")
print(f"Color de cabello: {seokjin.colorc} ")
print("-----Funciones para Seokjin-----")
seokjin.correr1092("Seokjin")
seokjin.cantar1092("Seokjin")
seokjin.bailar1092("Seokjin")
seokjin.escuchar1092("Seokjin")
seokjin.accion1092("Seokjin")
