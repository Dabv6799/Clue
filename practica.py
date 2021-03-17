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
        ale_luismi = random.randint(1,3)
        #ale_luismi = 1
        if ale_luismi == 1:
            print("Se encontró un cuerpo tan naranja como el sol, tenia rasgos de pelea,rasguños caracteristicos de uñas largas(o postizas),con varias lesiones punzantes en el torax")
            print("El cuerpo estaba entre el baño y el camerino de los participantes del comercial")
            self.aux_arma = 1
            self.aux_asesino = 3
            self.pista_luismi1()
            
        if ale_luismi == 2:
            print("El cuerpo de quien sería el niño di oro, estaba tirado en su camerino,se encontro una bebida alcoholica derramada y otra a medio llevar, presenta espuma en la boca por lo cual puede ser indicios de envenenamiento.")
            self.aux_arma = 3
            self.aux_asesino = 4
            self.pista_luismi2()
            
        if ale_luismi == 3:
            print("El cuerpo de luismi se estaba debajo de unas lonas en la bodega de utileria, casualmente en la bodega solo tienen sogas y palas,pero en este caso solo habia sogas")
            print("Presenta golpes contundentes en la nuca, posiblemente hechos con algun objeto lo suficientemente duro para realizar el daño")
            self.aux_arma = 5
            self.aux_asesino = 5
            self.pista_luismi3()

    #Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne se encontraba en el set de grabación(me incomoda ver que tiene uñas largas), dice que el solo quiere ser torero y que vio a Carmelita Salir del baño")
            print("Se encontró cerca de Chayanne una soga limpia y reluciente como el")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel se encontraba agitada, y sin sus tacones de 15cm punta de diamante importados GUCCI,ella dice que necesitaba meditar antes de grabar en su camerino")
            print("No se encontraron los tacones por ningun lado,pero afirma que vio a Tom Cruise mirar con envidia a Luismi")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom solo dijo cosas que no entendi porque no hablo ingles,pero con señas entendi que estaba en el area comun")
            print("Tenia las tijeras en las manos, tenian un olor peculiar a hierro, cabe mencionar que dice que con las tijeras corto carne de su comida")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmen como siempre me dijo 'Mijito',dice que vio de reojo a Luismi con Maribel,coqueteando,pero no esta segura porque tapo el baño,se fue rapido y corrió")
            print("Tambien comenta que Maribel aun tenia sus tacones puestos, por cierto el baño esta hecho un asco y como que la señora lo intento destapar con una pala")
        
        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne si se parece a mi, se lo presentare a mi mama, en fin, el dice que fue por unas bebidas para todos en el area comun, pero el no tomo nada porque es fitness y no era agua VOSS")
            print("Traia una soga, con la cual sujetó las bebidas para hacer malabares segun el, muy curioso :/ ")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel me dijo que su vestido se le estaba saliendo la etiqueta y que mientras estuvo cortandola, escucho cerca del camerino a Tom hablar con Luismi sobre una pelicula en la que aun no deciden quien de ellos dos sera el protagonista")
            print("A pesar de su edad se ve muy bien, por cierto,usó unas tijeras para cortar la etiqueta")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Ahora entiendo porque mi hermana ve sus peliculas diario, esta papucho,tiene aliento alcoholico,me dice que en efecto estuvo con Luismi en el camerino celebrando que le dieron el papel a Luismi")
            print("Se encontraron rastros de polvo de dudosa procedencia en su chaqueta de cuero, no puedo saber si es cocaina,harina,veneno,o algun tipo de polvos magicos")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmen se encontro todo este tiempo en la bodega de utileria encerrada,la pobre fue por una pala para el comercial y se le olvido que la puerta solo se abre desde afuera")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne,el que siempre dice que hay tiempo para bailar un vals, buena onda el tipo,dice que estuvo todo el tiempo en el baño debido a unas papas con chile de la esquina que le cayeron mal,y pues se volvio a meter al baño de hecho...")
            print("En el baño encontre veneno para ratas sin usar,sellado aun parece ser que en el set hay muchas ratas")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Señorita maribel pase la receta de la juventud eterna,ella me comentó que no vio en ningun momento a Luismi ya que estaba coqueteando con Tom Cruise en el set un rato")
            print("Tenia una soga en las manos pero no parece tener rastros de nada, al parecer la iba a usar en el comercial que iban a grabar")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise es muy alto comparado con mi primo el que dicen que se parece a el...curioso,el comenta que en efecto estuvo con maribel pero cuando fue hacia el Camerino vio a Carmen salir de la bodega con una pala,que porque la queria para plantar sus suculentas en su patio ")
            print("Tom no sabe decir 'Viva mexico y que chingue su madre el america'")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita salinas se veia mas rara de lo que ya se ve en sus memes, trae unos tacones bastante altos, creo que se los robo a Maribel no se ve que sean para ella")
            print("Afirma que estuvo en la bodega buscando los tacones pero en ningun momento supo decirme donde estaba la pala que debia estar en la bodega ya que ella afirma que cuando entró ya no habia palas.")

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
        #ale_luismi = random.randint(1,3)Esta linea se esta omitiendo por el momento 
        ale_chayanne = 1
        if ale_chayanne == 1:
            print("El torero se encontró sin vida en el set de grabación,mostraba signos de muerte por perdida de aire, algunos golpes en el rostro y lo que parecen ser cortes o rasguños en el cuello tambien")
            self.aux_arma = 2
            self.aux_asesino = 4
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

        if (self.arreglo_modific[self.per_mat-1] == 'Luismi'):
            print("¿Sera imprudente si le pregunto si su vida realmente fue como en la serie de netflix?,bueno en fin,Luismi afirma que se encontro todo el tiempo en su camerino ya que no le gusta convivir con la gente fuera de su horario de trabajo")
            print("No habia señales de que indicaran lo contrario")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel Guardia dice que no fue ella y que se encontro todo el tiempo en la bodega tratando de ponerse unos tacones de utileria que le indicaron quedarian mejor con us vestuario")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom cruise dice que estuvo rapido en el set pero que no duro mucho ya que es el que menos escenas grabaria porque cobra caro, pude notar que sus manos estaban raspadas y rojizas pero el afirma eso se debe a que el graba todas sus escenas sin dobles de accion")
            print("Habia una soga en el set un tanto desgastada como si alguien hubiera querido limparla con algun acido que la termino quemando")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            print("Carmelita Salinas afirma haber visto a Tom grabar algunas escenas con Chayanne y quedarse un rato ahi sin hacer nada despues,ella despues de eso fue al baño ya que no sentia muy bien al saber que fallecio Cepillin")
            print("Traía una pala y me dice que la uso para matar una rata que le salio en el baño,tiene sangre la pala de hecho,es muy sospechoso")

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
