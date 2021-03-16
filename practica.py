import random

class Historias:
    personaje = 0
    arma = 0
    matar = 0
    per_mat = 0
    arreglo_pers = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']
    arreglo_modific = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']
    arreglo_arma = ['1', '2','3','4','5']
    
#Este es para todos los pesonajes
    def ventana_ini(self):
        print("Elige a quien matar")
        for i in range(0,len(self.arreglo_pers)):
            print(i+1,".-", self.arreglo_pers[i])
        self.matar = int(input())
        self.arreglo_modific.pop(self.matar-1)

#---------------------------------------Este es solo para cuando matan a Luismi----------------------------------------------------------------
    def luismi(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_luismi = 1
        if ale_luismi == 1:
            self.pista_luismi1()
            
        if ale_luismi == 2:
            self.pista_luismi2()
            
        if ale_luismi == 3:
            self.pista_luismi3()

    #Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)
#-----------------------------------Aqui se termina el bloque de luismi --------------------------------------------



#Este es para todos los personajes 
    def acusar(self):
        print("Es momento que digas quien es el responsable de la muerte de ", self.arreglo_pers[self.matar])
        for i in range(0,len(self.arreglo_pers)):
            print(i+1,".-", self.arreglo_pers[i])
        self.personaje = int(input())

        print("Ahora selecciona el arma con la que mataron a la victima")
        for i in range(0, len(self.arreglo_arma)):
            print(i+1, ".-", self.arreglo_arma[i])
        self.arma = int(input())

        if self.personaje == 1 and self.arma == 1:
            print("Su respuesta fue correcta")
        else:
            print("La repuesta correcta es:")
            print("Como sucedieron los hechos ")

#---------------------------------------- Este es solo para Chayanne --------------------------------------------------
    def chayanne(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_chayanne = 1
        if ale_chayanne == 1:
            self.pista_chayanne1()
            
        if ale_chayanne == 2:
            self.pista_chayanne2()
            
        if ale_chayanne == 3:
            self.pista_chayanne3()

    #Estas son las narrativas 2 de Randon Cuando matan a Chayanne
    def pista_chayanne1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a Chayanne
    def pista_chayanne2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Chayanne
    def pista_chayanne3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de chayanne -------------------------------------------------



#-----------------------------------------------  Este es solo para Maribel guardia --------------------------------------------------
    def maribel(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_chayanne = 1
        if ale_chayanne == 1:
            self.pista_maribel1()
            
        if ale_chayanne == 2:
            self.pista_maribel2()
            
        if ale_chayanne == 3:
            self.pista_maribel3()

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_maribel1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_maribel2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Maribel
    def pista_maribel3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de Maribel -------------------------------------------------


#-----------------------------------------------  Este es solo para Tom Cruise --------------------------------------------------
    def tom(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_tom = 1
        if ale_tom == 1:
            self.pista_tom1()
            
        if ale_tom == 2:
            self.pista_tom2()
            
        if ale_tom == 3:
            self.pista_tom3()

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_tom1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_tom2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Maribel
    def pista_tom3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de Tom -------------------------------------------------


#-----------------------------------------------  Este es solo para carmelita  --------------------------------------------------
    def carmen(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_carmen = 1
        if ale_carmen == 1:
            self.pista_carmen1()
            
        if ale_carmen == 2:
            self.pista_carmen2()
            
        if ale_carmen == 3:
            self.pista_carmen3()

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_carmen1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_carmen2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Maribel
    def pista_carmen3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Aqui va la pista de Chayanne")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("luismi")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de carmen  -------------------------------------------------



#Esto es algo asi como el main
Clue = Historias()
Clue.ventana_ini()
print("Se acaba de cometer un homicidio y tu eres el encargado de averiguar quien fue el asesino y como lo mataron")
print("Se te iran dando una serie de pistas para determinar el asesinato")
print("¡SUERTE EN EL DESAFIO!")

#Este es para cuando queremos matar a Luismi
if Clue.matar == 1:
    Clue.luismi()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                Clue.pista_luismi1()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False

#Este es para cuando queremos matar a Chayane
if Clue.matar == 2:
    Clue.chayanne()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                Clue.pista_chayanne1()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False

#Este es para cuando queremos matar a Maribel Guardia
if Clue.matar == 3:
    Clue.maribel()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                Clue.pista_maribel1()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False

#Este es para cuando queremos matar a Tom Cruise
if Clue.matar == 4:
    Clue.tom()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                Clue.pista_tom1()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False

##Este es para cuando queremos matar a Carmelita Salinas
if Clue.matar == 5:
    Clue.carmen()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                Clue.pista_tom1()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False
