import random

class Tablero:
    def __init__(self) -> None:
        self.__tablero=[["·","A","B","C","D","E","F","G","H","I","J"],["1","^","^","^","^","^","^","^","^","^","^"],["2","^","^","^","^","^","^","^","^","^","^"],["3","^","^","^","^","^","^","^","^","^","^"],["4","^","^","^","^","^","^","^","^","^","^"],["5","^","^","^","^","^","^","^","^","^","^"],["6","^","^","^","^","^","^","^","^","^","^"],["7","^","^","^","^","^","^","^","^","^","^"],["8","^","^","^","^","^","^","^","^","^","^"],["9","^","^","^","^","^","^","^","^","^","^"],["10","^","^","^","^","^","^","^","^","^","^"]]
        self.__tableroRespuestas=[["·","A","B","C","D","E","F","G","H","I","J"],["1","^","^","^","^","^","^","^","^","^","^"],["2","^","^","^","^","^","^","^","^","^","^"],["3","^","^","^","^","^","^","^","^","^","^"],["4","^","^","^","^","^","^","^","^","^","^"],["5","^","^","^","^","^","^","^","^","^","^"],["6","^","^","^","^","^","^","^","^","^","^"],["7","^","^","^","^","^","^","^","^","^","^"],["8","^","^","^","^","^","^","^","^","^","^"],["9","^","^","^","^","^","^","^","^","^","^"],["10","^","^","^","^","^","^","^","^","^","^"]]

    def imprimir(self):
        for i in range(11):
            print(self.__tablero[i])
    def setPosicion(self,cord,simbolo):
        self.__tablero[cord[0]][cord[1]]=simbolo

    def colocarBarco(self,x,y):
        self.__tableroRespuestas[x][y]="B"
    def getSolucion(self):
        return self.__tableroRespuestas

class Barco:
    def __init__(self, longitud):
        self.__longitud=longitud
        self.__posiciones=[]
    
    def getPosiciones(self):
        return self.__posiciones

    def crear(self, tablero):
        v_h = random.randint(0, 1)

        if self.__longitud == 8:
            if v_h == 1:
                x = random.randint(1, 10)
                y = random.randint(1, 2)
                for i in range(8):
                    if tablero.getSolucion()[x][y + i] != "^":
                        return self.crear(tablero)  # Si la posición ya está ocupada, intenta crear el barco de nuevo
                for i in range(8):
                    tablero.colocarBarco(x, y + i)
            else:
                y = random.randint(1, 10)
                x = random.randint(1, 2)
                for i in range(8):
                    if tablero.getSolucion()[x + i][y] != "^":
                        return self.crear(tablero)
                for i in range(8):
                    tablero.colocarBarco(x + i, y)
        if self.__longitud == 3:
            if v_h == 1:
                x = random.randint(1, 10)
                y = random.randint(1, 7)
                for i in range(3):
                    if tablero.getSolucion()[x][y + i] != "^":
                        return self.crear(tablero)  # Si la posición ya está ocupada, intenta crear el barco de nuevo
                for i in range(3):
                    tablero.colocarBarco(x, y + i)
            else:
                y = random.randint(1, 10)
                x = random.randint(1, 7)
                for i in range(3):
                    if tablero.getSolucion()[x + i][y] != "^":
                        return self.crear(tablero)
                for i in range(3):
                    tablero.colocarBarco(x + i, y)
        if self.__longitud == 2:
            if v_h == 1:
                x = random.randint(1, 10)
                y = random.randint(1, 8)
                for i in range(2):
                    if tablero.getSolucion()[x][y + i] != "^":
                        return self.crear(tablero)  # Si la posición ya está ocupada, intenta crear el barco de nuevo
                for i in range(2):
                    tablero.colocarBarco(x, y + i)
            else:
                y = random.randint(1, 10)
                x = random.randint(1, 8)
                for i in range(2):
                    if tablero.getSolucion()[x + i][y] != "^":
                        return self.crear(tablero)
                for i in range(2):
                    tablero.colocarBarco(x + i, y)


class Jugador:
    def __init__(self,tablero):
        self.__barco8=Barco(8)
        self.__barco3_1=Barco(3)
        self.__barco3_2=Barco(3)
        self.__barco2_1=Barco(2)
        self.__barco2_2=Barco(2)
        self.__tablero=tablero

        self.__barco8.crear(self.__tablero)
        self.__barco3_1.crear(self.__tablero)
        self.__barco3_2.crear(self.__tablero)
        self.__barco2_1.crear(self.__tablero)
        self.__barco2_2.crear(self.__tablero)

        self.__tocados8=0
        self.__tocados3_1=0
        self.__tocados3_2=0
        self.__tocados2_1=0
        self.__tocados2_2=0
        self.__vida=36
    
    def comprobarTiro(self,cord):
        acierto=False
        tableroR=self.__tablero.getSolucion()
        if tableroR[cord[0]][cord[1]]=="B":
            acierto=True

        if(acierto):
            self.__tablero.setPosicion(cord,"⛵")
            print("Tocado")
            self.__vida-=1
        else:
            self.__tablero.setPosicion(cord,"🌊")
            print("Agua")
    
    def perder(self):
        if(self.__vida==0):
            return True
        else:
            return False
    def getTablero(self):
        return self.__tablero



#JUEGO
print("***********************************")
print("|         HUNDIR LA FLOTA         |")
print("***********************************")

tablero_j1=Tablero()
tablero_j2=Tablero()

j1=Jugador(tablero_j1)
j2=Jugador(tablero_j2)


print("Elije un modo de juego:")
print("1. 1 Jugador")
print("2. 2 Jugadores")

numJugadores=int(input(""))

fin=False

while(fin==False):
      cord=[]
      print("Tablero Jugador 1")
      print("------------------")
      tableroJ1=j1.getTablero()
      tableroJ1.imprimir()

      print("Tablero Jugador 2")
      print("------------------")
      tableroJ2=j2.getTablero()
      tableroJ2.imprimir()

      x=int(input("Jugador 1: Introduce la coordenada x ->"))
      y=int(input("Jugador 1: Introduce la coordenada y ->"))
      cord=[y,x]

      j2.comprobarTiro(cord)
      cord=[]
      if(j2.perder==True):
          print("Jugador 2 ha ganado")
          fin=True
      if(numJugadores==2):
          x=int(input("Jugador 2: Introduce la coordenada x ->"))
          y=int(input("Jugador 2: Introduce la coordenada y ->"))
      else:
          x=random.randint(1,10)
          y=random.randint(1,10)

      cord=[y,x]
      j1.comprobarTiro(cord)

      if(j1.perder==True):
          print("Jugador 2 ha ganado")
          fin=True
          


          





