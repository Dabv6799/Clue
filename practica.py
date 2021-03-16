#import random


class Historias:
    personaje = ""
    arma = ""
    matar = ""
    arreglo_pers = (["Luismi", "Chayanne", "Maribel Guardia", "Tom cruise", "Carmelita Salinas"])

    def ventana_ini(self):
        print("Elige a quien matar")
        matar = int(input())


    def selec_nombre(self):
        print("Selecciona el personaje que fue el culpable")
        print("1.-Luismi")
        print("2.-Chayanne")
        print("3.-Maribel Guardia")
        print("4.-Tom cruise")
        print("5.-Carmelita Salinas")
        self.personaje = int(input())
        for n in range(0,len(self.arreglo_pers)):
            if (n == self.personaje):
                n=n-1
                np.delete(self.arreglo_pers, n)


    def select_arma(self):
        print("Con que arma fue asesinado")
        print("1.-")
        print("2.-Pala")
        print("3.-Jeringa")
        print("4.-Soga")
        print("5.-Taladro")
        self.arma = int(input())

    def luismi(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        ale_luismi = random.randint(1,3)
        if ale_luismi() == 1:
            #def historia1_luismi():
            pass
        if ale_luismi() == 2:
            #def historia2_luismi():
            pass
        if ale_luismi() == 3:
            #def historia3_luismi():
            pass

    def pista(self):
        print("¿A quien deseas preguntar?")
        print("1.-Chayanne")
        print("2.-Maribel Guardia")
        print("3.-Tom cruise")
        print("4.-Carmelita Salinas")




Clue = Historias()
Clue.ventana_ini()

Clue.ventana_ini()
print("Se acaba de cometer un homicidio y tu eres el encargado de averiguar quien fue el asesino y como lo mataron")
print("Se te iran dando una serie de pistas para determinar el asesinato")
print("¡SUERTE EN EL DESAFIO!")

if Clue.matar == 1:
    Clue.luismi()

if Clue.matar == 2:
    pass

if Clue.matar == 3:
    pass

if Clue.matar == 4:
    pass

if Clue.matar == 5:
    pass
