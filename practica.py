import random

class Historias:
    personaje = 0
    arma = 0
    aux_arma = 0
    aux_asesino = 0
    matar = 0
    per_mat = 0
    arreglo_pers = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']
    arreglo_modific = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']
    arreglo = ['Luismi', 'Chayanne', 'Maribel Guardia', 'Tom cruise', 'Carmelita Salinas']
    arreglo_arma = ['Tacon de aguja', 'Soga','Veneno','Tijeras','Pala']
    
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
        ale_luismi = random.randint(1,3)
        ale_luismi = 1
        if ale_luismi == 1:
            self.aux_arma = 1
            self.aux_asesino = 2
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
        print("Es momento que digas quien es el responsable de la muerte de ", self.arreglo_pers[self.matar-1])
        self.arreglo_pers.pop(self.matar-1)
        for i in range(0,len(self.arreglo_pers)):
            print(i+1,".-", self.arreglo_pers[i])
        self.personaje = int(input())

        print("Ahora selecciona el arma con la que mataron a la victima")
        for i in range(0, len(self.arreglo_arma)):
            print(i+1, ".-", self.arreglo_arma[i])
        self.arma = int(input())
                        
        print(self.aux_asesino, "posicion de arma")
            
        if self.personaje == self.aux_asesino and self.arma == self.aux_arma:
            print("Perro, lo descubriste")
            print("Ya vente a CSI o Criminal Minds")
            
        elif self.personaje == self.aux_asesino or self.arma == self.aux_arma:
            print("No estuviste taaaaaaaan mal")
            print("El asesino es: ", self.arreglo[self.personaje-1])
            print("El arma es: ", self.arreglo_arma[self.aux_arma-1])
            print("Mereces ser policia de barrio")
            
        else:
            print("Te fue muy mal")
            print("El asesino es: ", self.arreglo[self.personaje])
            print("El arma es: ", self.arreglo_arma[self.aux_arma-1])
            print("Dedicate a otras cosas")


#---------------------------------------- Este es solo para Chayanne --------------------------------------------------
    def chayanne(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        ale_chayanne = random.randint(1,3)

        if ale_chayanne == 1:
            print("Se encontro un cuerpo tirado a la mitad del set de grabacion, el cuerpo lleva horas tirado en ese lugar creyendo que era una actuacion")
            print("Al revisarlo nos percatamos que es el hermoso Chayanne, que de hermoso ya no tiene nada porque su rostro fue destruido")
            print("Y los cortes en su cara son bastante profundos")
            self.aux_arma = 4
            self.aux_asesino = 4
            self.pista_chayanne1()

#Estas son las narrativas 2 de Randon Cuando matan a Chayanne
    def pista_chayanne1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Al entrevistar a Maribel Guardia nos menciona que ella se encontraba en el area comun limpiando sus tacones, esto porque habia teniado un accidente con la comida")
            print("Y que antes, habia visto a Chayanne ensayar para la presentacion del comercial")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Notamos un comportamiento extraño en la actitud de Tom Cruise, al entrevistarlo nos menciona que esta muy desconcertado con la muerte de su amigo")
            print("Nos dice que en el dia no lo habia visto porque tenia gran malestar estomacal por ello la mayor parte del dia estuvo en el baño")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Llegamos a donde esta carmelita, ella se encontraba cortando hilo para tejer pero notamos algo extraño sus tijeras tenian una mancha entraña en la punta")
            print("Nos menciona solo queria relajarse un poco y es por ello que esta tejiendo")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Cuando llegamos al camerino de luismi, el se encontraba observandose en el espejo, se le veia el amor en su rostro, todo estaba bastante limpio y tranquilo")
            print("Nos limitamos a hacer muchas preguntas, ya que dijo que estuvo practicando sus expresiones frente al espejo")
        self.arreglo_modific.pop(self.per_mat-1)
#----------------------------------------------- Aqui termina el bloque de chayanne -------------------------------------------------



#-----------------------------------------------  Este es solo para Maribel guardia --------------------------------------------------
    def maribel(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        ale_maribel = random.randint(1,3)
        if ale_maribel == 1:
            print("Se encontro el cuerpo de maribel postrado a la mitad del pasillo, su cuerpo se ve bastante amarillo no sabemos si es la edad o si tomo algo")
            print("tambien se encontraron algunos golpes pero creemos que los golpes son de la caida ")
            self.aux_arma = 3
            self.aux_asesino = 1
            self.pista_maribel1()           

#Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_maribel1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne nos dice que hablo con maribel antes en el area comun, ellos hablaban de sus dietas y compartieron un poco de sus alimentos")
            print("Tambien nos menciona que muchos decian que ella y Tom tenian bastantes problemas")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom aclara que el y ella, definitivamente tenian bastantes problemas pero que el habia estado buscando su vestuario en la bodega")
            print("El llevaba una soga dice 'Que es parte del vestuario', pero que vio a luismi y ella hablar cerca del baño ")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita muy amable como siempre nos recibio de muy buena manera, ella tenia unos tacones muy bonitos que eran de maribel")
            print("dijo que los habia pedido prestado y la estuvo buscando para entregarlos pero nunca la encontro")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("A luismi nos costo bastante encontralo, parecia que se estaba escondiendo de alguien 'sospechoso no?' aparte tenia un olor extraño")
            print("Dice que si hablaron no nos dijo mucho, pero que le dio a probar un poco de su comida porque ella estaba muy hambrienta")
        self.arreglo_modific.pop(self.per_mat-1)
        
        #----------------------------------------------- Aqui termina el bloque de Maribel -------------------------------------------------


#-----------------------------------------------  Este es solo para Tom Cruise --------------------------------------------------
    def tom(self):
        print ("NARRATIVA DE COMO SUCEDIERON LOS HECHOS")
        ale_tom = random.randint(1,3)
        ale_tom = 1
        if ale_tom == 1:
            print("Acaba de suceder una de las peores tragedias, Tom Cruise esta muerto se encontro su cuerpo tirado en el camerino, este presenta marcas alrededor del cuello")
            print("Era el actor principal en una pelicula y todo pareciera que me suicido pero la escena del crimen demostraba lo contrario")
            self.aux_arma = 2
            self.aux_asesino = 2
            self.pista_tom1()
            
        if ale_tom == 2:
            print("Esta es sin duda la peor escena del crimen, se encontro a Tom Cruise un ojo de fuera pareciera que algo le atraveso el craneo, el se encontraba sentado en area comun")
            print("Aun no estamos seguros como sucedieron los hechos ")
            self.aux_arma = 1
            self.aux_asesino = 1
            self.pista_tom2()
            

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_tom1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Cuando se entrevisto a chayanne notamos que en sus brazos tenia rasguños y algunas marcas extrañas, menciona que es parte de pelicula en la que trabaja")
            print("Dice que no habia vistro a Tom y que estuvo en el set de grabaciones haciendo su pelicula")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Al llegar con ella nos menciono que Chayanne en ningun momento habia estado en el set, que ella estuvo pasando del set al area comun")
            print("Aunque ella llevaba una pala un tanto extraña, no dio explicacion de la pala")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("La señora Carmen nos dijo que ella no habia visto nada que estuvo en la bodega junto con luismi buscando utileria para la pelicula que iba a grabar Tom")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Al llegar con luismi con confirma lo que dijo la señora Carmen pero nos da un dato extra, menciona que el papel principal que era de Tom, chayanne lo habia anelado durante mucho tiempo")
            print("Y que cuando lo tuvo Tom, chayanne se enojo muchisimo")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_tom2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne dijo que llevaba bastante prisa y no tenia mucho tiempo de hablar, llevaba una pala y dijo que tenia que ir a plantar arboles")
            print("Dijo que la ultima vez que hablo con chayanne estaba en su camerino hablando y que se veia muy feliz")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Estaba muy triste porque sus tacones estaban extraviados y los habia buscado todo el dia dentro de su camerino ")
            print("Y que la ultima vez que vio a Tom fue discutiendo con luismi cerca del area comun, pero no le habia tomado mucha importanci, dice que en ese momento aun tenia sus tacones")
       
        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita dijo que vio los tacones de Maribel en el area comun que ahi los habia dejado y que cuando ella salio, estaba llegando Tom y Luismi")
            print("despues de eso ella se retiro para dejarlos hablar con tranquilidad")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Luismi menciono que el habia platicando con Tom pero despues de un rato en el area comun se retiro a su camerino")
            print("Notamos que en su zapato tiene un poco de sangre, dijo que era un poco de sangre de su nariz")

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
