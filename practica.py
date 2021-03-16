import random
import os


class Historias:
    personaje = 0
    arma = 0
    matar = 0
    arreglo_pers = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']

    def ventana_ini(self):
        print("Elige a quien matar")
        for n in range(0, len(self.arreglo_pers)):
            print(n+1, ".-",self.arreglo_pers[n])
        self.matar = int(input())
        self.arreglo_pers[n].pop(n)
        os.system ("cls") 
        
        print("Se acaba de cometer un homicidio y tu eres el encargado de averiguar quien fue el asesino y como lo mataron")
        print("Se te iran dando una serie de pistas para determinar el asesinato")
        print("¡SUERTE EN EL DESAFIO!")
        os.system ("cls") 
        
        if (self.matar == 1):
            Clue.luismi()

        if self.matar == 2:
            pass
        
        if self.matar == 3:
            pass
        
        if self.matar == 4:
            pass
        
        if self.matar == 5:
            pass


    def selec_nombre(self):
        print("Selecciona el personaje al que quieres interrogar >:|")
        for n in range(0,len(self.arreglo_pers)):
            print(self.arreglo_pers[n])
            #if n == :
             #   print(n+1, ".-", self.arreglo_pers[n])
            


    def select_arma(self):
        print("Con que arma fue asesinado")
        print("1.-")
        print("2.-Pala")
        print("3.-Jeringa")
        print("4.-Soga")
        print("5.-Taladro")
        self.arma = int(input())


    def historia1_luismi(self):
        os.system ("cls") 
        
    def luismi(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)
        ale_luismi = 1
        if ale_luismi == 1:
            self.selec_nombre()
        if ale_luismi == 2:
            #def historia2_luismi():
            pass
        if ale_luismi == 3:
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




