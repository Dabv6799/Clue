import random
import os
class Historias:
    personaje = 0
    arma = 0
    aux_arma = 0
    aux_asesino = 0
    matar = 0
    per_mat = 0
    decision = 0
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
            self.decision = 1
           # print(self.decision)
            os.system('cls')
            print("Pobre Luis Miguel...se encontró un cuerpo tan naranja como el sol, tenia rasgos de pelea,rasguños caracteristicos de uñas largas(o postizas),con varias lesiones punzantes en el torax")
            print("El cuerpo estaba entre el baño y el camerino de los participantes del comercial")
            self.aux_arma = 1
            self.aux_asesino = 2
            self.pista_luismi1()
            
        if ale_luismi == 2:
            self.decision = 2
            os.system('cls')
            print("El cuerpo de quien sería el niño di oro(Luismi), estaba tirado en su camerino,se encontro una bebida alcoholica derramada y otra a medio llenar, presenta espuma en la boca por lo cual puede ser indicios de envenenamiento.")
            self.aux_arma = 3
            self.aux_asesino = 3
            self.pista_luismi2()
            
        if ale_luismi == 3:
            self.decision = 3
            os.system('cls')
            print("El cuerpo de Luismi estaba debajo de unas lonas en la bodega de utileria, casualmente en la bodega solo tienen sogas y palas,pero en este caso solo habia sogas")
            print("Presenta golpes contundentes en la nuca, posiblemente hechos con algun objeto lo suficientemente duro para realizar el daño")
            self.aux_arma = 5
            self.aux_asesino = 4
            self.pista_luismi3()

    #Estas son las narrativas 2 de Randon Cuando matan a Luismi
    def pista_luismi1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')
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
        os.system('cls')
        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne si se parece a mi, tal vez y si sea mi papa como decia mi mamá, en fin, el dice que fue por unas bebidas para todos en el area comun, pero el no tomo nada porque es fitness y no era agua VOSS")
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

        os.system('cls')

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

        os.system('cls')

        print("Es momento que digas quien es el responsable de la muerte de ", self.arreglo_pers[self.matar-1])
        self.arreglo_pers.pop(self.matar-1)
        for i in range(0,len(self.arreglo_pers)):
            print(i+1,".-", self.arreglo_pers[i])
        self.personaje = int(input())

        os.system('cls')

        print("Ahora selecciona el arma con la que mataron a la victima")
        for i in range(0, len(self.arreglo_arma)):
            print(i+1, ".-", self.arreglo_arma[i])
        self.arma = int(input())
                        
        print(self.aux_asesino, "posicion de arma")
            
        if self.personaje == self.aux_asesino  and self.arma == self.aux_arma:

            os.system('cls')
            print(self.personaje, "posicion de asesino escogido")
            print(self.aux_asesino, "posicion de asesino")
            print("Perro, lo descubriste")
            print("Ya vente a CSI o Criminal Minds")
            
        elif self.personaje == self.aux_asesino or self.arma == self.aux_arma:

            os.system('cls')
            print(self.personaje, "posicion de asesino escogido")
            print(self.aux_asesino, "posicion de asesino")
            print("No estuviste taaaaaaaan mal")
            print("El asesino es: ", self.arreglo[self.personaje-1])
            print("El arma es: ", self.arreglo_arma[self.aux_arma-1])
            print("Mereces ser policia de barrio")
            
        else:

            os.system('cls')
            print(self.personaje, "posicion de asesino escogido")
            print(self.aux_asesino, "posicion de asesino")
            print("Te fue muy mal")
            print("El asesino es: ", self.arreglo[self.personaje])
            print("El arma es: ", self.arreglo_arma[self.aux_arma-1])
            print("Dedicate a otras cosas")


#---------------------------------------- Este es solo para Chayanne --------------------------------------------------
    def chayanne(self):
        ale_chayanne = random.randint(1,3)
        if ale_chayanne == 1:
            os.system('cls')
            self.decision = 1
            
            print("El torero se encontró sin vida en el set de grabación,mostraba signos de muerte por perdida de aire, algunos golpes en el rostro y lo que parecen ser cortes o rasguños en el cuello tambien")
            self.aux_arma = 2
            self.aux_asesino = 3
            self.pista_chayanne1()
            
        if ale_chayanne == 2:
            os.system('cls')
            self.decision = 2
            
            print("Se encontro un cuerpo tirado a la mitad del set de grabacion, el cuerpo lleva horas tirado en ese lugar creyendo que era una actuacion")
            print("Al revisarlo nos percatamos que es el hermoso Chayanne, que de hermoso ya no tiene nada porque su rostro fue destruido")
            print("Y los cortes en su cara son bastante profundos")
            self.aux_arma = 4
            self.aux_asesino = 3
            self.pista_chayanne2()
            

    #Estas son las narrativas 2 de Randon Cuando matan a Chayanne
    def pista_chayanne1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())

        os.system('cls')

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

        os.system('cls')

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
        ale_maribel = random.randint(1,3)
        print(ale_maribel)
        if ale_maribel == 1:
            self.decision = 1
            os.system('cls')
            print("Se encontro el cuerpo de maribel postrado a la mitad del pasillo, su cuerpo se ve bastante amarillo no sabemos si es la edad o si tomo algo")
            print("tambien se encontraron algunos golpes pero creemos que los golpes son de la caida ")
            self.aux_arma = 3
            self.aux_asesino = 1
            self.pista_maribel1()      
            
        if ale_maribel == 2:
            os.system('cls')
            print("Se encontro a la señora Maribel tirada en el baño con signos de agresión fisica, los senos rebentados y la cara aboyada")
            print("También tiene la nariz rota y se muestra signos de un golpe plano")
            self.aux_arma = 5
            self.aux_asesino = 2
            self.decision = 2
            self.pista_maribel2()

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_maribel1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            os.system('cls')
            print("Chayanne nos dice que hablo con maribel antes en el area comun, ellos hablaban de sus dietas y compartieron un poco de sus alimentos")
            print("Tambien nos menciona que muchos decian que ella y Tom tenian bastantes problemas")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            os.system('cls')
            print("Tom aclara que el y ella, definitivamente tenian bastantes problemas pero que el habia estado buscando su vestuario en la bodega")
            print("El llevaba una soga dice 'Que es parte del vestuario', pero que vio a luismi y ella hablar cerca del baño ")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
            os.system('cls')
            print("Carmelita muy amable como siempre nos recibio de muy buena manera, ella tenia unos tacones muy bonitos que eran de maribel")
            print("dijo que los habia pedido prestado y la estuvo buscando para entregarlos pero nunca la encontro")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            os.system('cls')
            print("A luismi nos costo bastante encontralo, parecia que se estaba escondiendo de alguien 'sospechoso no?' aparte tenia un olor extraño")
            print("Dice que si hablaron no nos dijo mucho, pero que le dio a probar un poco de su comida porque ella estaba muy hambrienta")
        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_maribel2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
           
            print("Chayanne menciono que Maribel y el no mantenian una relación cercana y estuvo en el set de grabación cuando pasaron los hechos")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
           
            print("Tom menciono que vio a Chayanne salir del vestidor de Maribel molesto")

        elif(self.arreglo_modific[self.per_mat-1] == 'Carmelita Salinas'):
           
            print("Carmelita mencino que no se encontraba en el lugar de hecho fue a pedir una pala a la bodega")
            print("Pero le dijeron que Chayanne ya habia solicitado una")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
           
            print("Luismi menciono haber visto a Maribel momentos antes de su muerte, estuvieron charlando")
            print("Pero el tuvo una emergencia en el set de grabación y la dejo a solas")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de Maribel -------------------------------------------------


#-----------------------------------------------  Este es solo para Tom Cruise --------------------------------------------------
    def tom(self):
        ale_tom = random.randint(1,3)
        if ale_tom == 1:
            self.decision = 1
            os.system('cls')
            print("Acaba de suceder una de las peores tragedias, Tom Cruise esta muerto se encontro su cuerpo tirado en el camerino, este presenta marcas alrededor del cuello")
            print("Era el actor principal en una pelicula y todo pareciera que me suicido pero la escena del crimen demostraba lo contrario")
            self.aux_arma = 2
            self.aux_asesino = 2
            self.pista_tom1()
            
        if ale_tom == 2:
            self.decision = 2
            os.system('cls')
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
        os.system('cls')

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
        os.system('cls')

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
        ale_carmen = random.randint(1,3)
        #ale_carmen = 1
        if ale_carmen == 1:
            os.system('cls')
            print("Se encontro a la señora diputada con signos de asfixia con un color morado que creo se debe por la axfixia")
            self.aux_arma = 2
            self.aux_asesino = 3
            self.decision = 1
            self.pista_carmen1()
            
        if ale_carmen == 2:
            os.system('cls')
            print("La Sra. Diputada fue encontrada en el área común en un charco de sangre")
            print("Tenía lesiones punzocortantes en el área toraxica y en el craneo")
            print("Fue un poco terrorifico ver la cantidad de lesiones que tenía")
            self.aux_arma = 4
            self.aux_asesino = 1
            self.decision = 2
            self.pista_carmen2()
            
        if ale_carmen == 3:
            os.system('cls')
            print("Se encontro a una señora de aproximadamente 87 años de edad sin signos de vitales, además se encontro una pintura de ella pintada en oleo")
            print("La señora presenta espuma en la boca, parecia que tenía rabia")
            print("no presentaba pigmentación en los globulos oculares")
            self.aux_arma = 3
            self.aux_asesino = 4
            self.decision = 3
            self.pista_carmen3()

    #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_carmen1(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("El papucho de todas las señoras nos menciono que en el momento de grabar la escena del comercial faltaba una soga")
            print("También nos dijo que Maribel Guardia tuvo una polemica pelea con la diputada porque según menciona la señora era una chismosa y se entrometia en la vida de los demás")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("El testimonio de la Sra. Maribel fue que ella y Carmen eran muy buenas amigas, siempre iban de compras y a comer")
            print("Nos dijo que Carmelita tomaba muchas pastillas")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom aclaro que él y Luismi estaban en los vestidores, según aclaro Luismi se puso los tacones de maribel para ver si le quedaban")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Luismi dijo que vio a dirijirse al baño a Maribel")
            print("Menciono algo muy inquietante, dijo que se ve bien con tacones")

        self.arreglo_modific.pop(self.per_mat-1)


 #Estas son las narrativas 2 de Randon Cuando matan a maribel
    def pista_carmen2(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne menciono que el estuvo en el baño rebentando una espinilla que le salio en el menton")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel menciono que vio salir a Carmelita salir de su camerino hacia el área común")
            print("Adjunto que vio a Luismi salir detras de ella")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom menciono que Carmelita Y Luismi mantenian una relación extralaboral")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Luismi menciono que estaba en el baño cuando pasaron los hechos, además se notaba algo agitado")

        self.arreglo_modific.pop(self.per_mat-1)

#Estas son las narrativas 2 de Randon Cuando matan a Maribel
    def pista_carmen3(self):
        print("Entrevista a las personas que estuvieron cerca de la escena")
        print("¿A quien deseas entrevistar?")
        for i in range(0,len(self.arreglo_modific)):
            print(i+1,".-", self.arreglo_modific[i])
        self.per_mat = int(input())
        os.system('cls')

        if (self.arreglo_modific[self.per_mat-1] == 'Chayanne'):
            print("Chayanne menciono que Tom Cruise tenía una fuerte rabía por la doñita")

        elif (self.arreglo_modific[self.per_mat-1] == 'Maribel Guardia'):
            print("Maribel menciono que ella fue quien encontro el cadaver, agrego que encontro un pequeño frasco de duddosa procedencia")
            print("Se sabe que la doña tomaba medicina para el corazón, sin embargo, jamás he visto esta marca en un medicamento")

        elif (self.arreglo_modific[self.per_mat-1] == 'Tom cruise'):
            print("Tom menciono que el se encontraba en el set de grabación, realizando el sketch del granjero ")

        elif (self.arreglo_modific[self.per_mat-1] == "Luismi"):
            print("Luismi dijo que vio a Tom con un frasco de medicamentos, se mostro desconcertado porque no sabía que el tomará algo")

        self.arreglo_modific.pop(self.per_mat-1)

#----------------------------------------------- Aqui termina el bloque de carmen  -------------------------------------------------



#Esto es algo asi como el main
Clue = Historias()
Clue.ventana_ini()
os.system('cls')
print("Se acaba de cometer un homicidio y tu eres el encargado de averiguar quien fue el asesino y que arma utilizaron en el asesinato")
print("Se te iran dando una serie de pistas en base a los personajes que decidas entrevistar para determinar quien fue el asesino.")
'''print("Cuentas con la siguiente informacion para empezar: ")
print("Personajes:")
print("1. Luismi \n2. Chayanne\n3. Maribel Guardia\n4. Tom Cruise\n5. Carmen Salinas")
print("Armas:")
print("1. Tacon de aguja\n2. Soga\n3. Veneno\n4. Tijeras\n5. Pala")'''
print("¡SUERTE EN EL DESAFIO!(Presiona cualquier tecla para continuar)")
input()

#Este es para cuando queremos matar a Luismi
if Clue.matar == 1:
    Clue.luismi()
    ciclo = True
    while ciclo:
        print("Con los datos encontrados en la entrevita realizada a uno de los sospechosos")
        print("¿Quieres entrevistar a otro de los sospechosos o acusar al culpable?")
        print("1.-Otra pista")
        print("2.-Declarar al culpable")
        cos = int(input())
        os.system('cls')
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                #print(Clue.decision, "dime que esta pasando")
                if Clue.decision == 1:
                    Clue.pista_luismi1()
                elif Clue.decision == 2:
                    Clue.pista_luismi2()
                elif Clue.decision == 3:
                    Clue.pista_luismi3()
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
        os.system('cls')
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                if Clue.decision == 1:
                    Clue.pista_chayanne1()
                elif Clue.decision == 2:
                    Clue.pista_chayanne2()
                
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
        os.system('cls')
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                if Clue.decision == 1:
                    Clue.pista_maribel1()
                elif Clue.decision == 2:
                    Clue.pista_maribel2()
                
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
        os.system('cls')
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                if Clue.decision == 1:
                    Clue.pista_tom1()
                elif Clue.decision == 2:
                    Clue.pista_tom2()
                
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
        os.system('cls')
        if cos == 1:
            if len(Clue.arreglo_modific) == 0:
                print("Entrevistaste a todos los sospechosos, tendras que acusar al culpable")
                Clue.acusar() 
                ciclo = False
            else:
                if Clue.decision == 1:
                    Clue.pista_carmen1()
                elif Clue.decision == 2:
                    Clue.pista_carmen2()
                elif Clue.decision == 3:
                    Clue.pista_carmen3()
                
        if cos == 2:
            Clue.acusar()
            ciclo = False
