##############
# PROVA PROF #
##############
""" PROBLEMA 1 """
def checkString(str, alphaCounter, digitCounter):
# @param str : Str
# @param alphaCounter : List
# @param digitCounter : List
    lenght = len(str)
    if lenght == 0:
        return True
    elif lenght == 1:
        return alphaCounter == digitCounter
    else:
        if str[0].isalpha():
            alphaCounter = alphaCounter + 1
        elif str[0].isdigit():
            digitCounter = digitCounter + 1
        return checkString(str[1:], alphaCounter, digitCounter)

def prova1Problem1():
    print("#### PROBLEMA 1 ####")
    string = "abcd1234"
    print(checkString(string, 0, 0))
    string = "abcd123"
    print(checkString(string, 0, 0))
    string = "abc1234"
    print(checkString(string, 0, 0))
    string = "a!!1!!a!!1"
    print(checkString(string, 0, 0))
#prova1Problem1():



""" PROBLEMA 2 """
def foo(x, y=10) :
# @param x: int
# @param y: int
# @return int
    y = y - 10
    return x+y
# DOMANDA: quale valore viene assegnato alla variabile x nel comando x = foo(10,10) ? Motivare la risposta
# ERRORE, è presente un errore di semantica nella prima linea, perchè è vero che quella è un'espressione, ma
# non si svolge un assegnamento in questo modo
def prova1Problem2():
    print("#### PROBLEMA 2 ####")
    print(foo(10, 10))
#prova1Problem2():


""" PROBLEMA 3 """
# TODO



""" PROBLEMA 4 """
def prova1Problema4a():
    print("#### PROBLEMA 4a ####")
    def start():
        a = 'a'
        R(a)
        print(a)

    def R(x): # x = 'a'
        a = 'B'
        Q()
        x = a
        print(x)

    def Q():
        global a
        print(a)
        a = 'b'

    start() # A, B, a

def prova1Problema4b():
    print("#### PROBLEMA 4b ####")
    def start():
        a = 'a'
        R(a)
        print(a)
    def R(x):
        a = 'B'
        Q()
        x = a
        print(x)
    def Q():
        # global a
        print(a)
        a = 'b'
    start() # errore il parametro referenziato prima dell'assegnamento
#a = 'A'
#prova1Problema4a()
#a = 'A'
#prova1Problema4b()





""" PROBLEMA 5 """
class PoligonoRegolare:
    def __init__(self, numeroLati, lunghezzaLato):
    # @param numeroLati : Int
    # @param lunghezzaLato : Int
        self.sides = numeroLati
        self.sideLenght = lunghezzaLato

    def getPerimetro(self):
        return self.sideLenght * self.sides
    def getSideLenght(self):
        return self.sideLenght

class Quadrato (PoligonoRegolare):
    def __init__(self, lunghezzaLato):
    # @param lunghezzaLato : Int
        super().__init__(4, lunghezzaLato)

    def getArea(self):
        return self.sideLenght ** 2


def prova1Problem5():
    print("#### PROBLEMA 5 ####")
    poly = PoligonoRegolare(5, 10)
    print("Il perimetro del poligono regolare di lato", poly.getSideLenght(), "è: ", poly.getPerimetro())
    sqre = Quadrato(8)
    print("Il perimetro del quadrato di lato", sqre.getSideLenght(), "è: ", sqre.getPerimetro())
    print("L'area invece è: ", sqre.getArea())
#prova1Problem5()




""" PROBLEMA 6 """
def check(pict):
# @param pict : Picture
    for y in range(0, getHeight(pict)):
        if checkRow(pict, y):
            return True
    return False

def checkRow(pict, y):
# @param pict : Picture
# @param row : int
    firstPix = getPixel(pict, 0, y)
    for x in range(1, getWidth(pict)):
        pix = getPixel(pict, x, y)
        color = getColor(pix)
        if not color == getColor(firstPix):
            return False
    return True

def prova1Problem6():
    print("#### PROBLEMA 6 ####")
    colors = [red, green, blue, yellow, black, cyan, white]
    import random
    hw = 50
    pict = makeEmptyPicture(hw,hw)
    for x in range(0, hw):
        for y in range(0, hw):
            pix = getPixel(pict, x, y)
            setColor(pix, random.choice(colors))
    print(check(pict))


    pict = makeEmptyPicture(hw,hw, white)
    for y in range(0, hw-1):
      setColor(getPixel(pict, 1, y), black)
    print(check(pict))
#prova1Problem6()





""" PROBLEMA 7 """
class CustomTuple:

    def __init__(self, lenght):
        self.myTuple = ()
        for i in range(0, lenght):
            self.myTuple = self.myTuple + (0,)

    def display(self):
        print (self.myTuple)

    def edit(self, k, i):
        newTuple = ()
        for j in range(0, len(self.myTuple)):
            elem = self.myTuple[j]
            if elem == k:
                newTuple = newTuple + (elem + self.myTuple[i],)
            else:
                newTuple = newTuple + (elem,)
        self.myTuple = newTuple

class ChildCustomTuple (CustomTuple):
    def __init__(self, lenght, firstElem):
        super().__init__(lenght-1)
        self.myTuple = (firstElem,) + self.myTuple

def prova1Problem7():
    print("#### PROBLEMA 7 ####")
    customTuple = CustomTuple(10)
    customTuple.display()
    customTuple.edit(0, 1)
    customTuple.display()

    childCustomTuple = ChildCustomTuple(10, 3)
    childCustomTuple.display()
    childCustomTuple.edit(3, 0)
    childCustomTuple.display()
#prova1Problem7()





""" PROBLEMA 8 """
def luminosity(pix):
# @param pix : Pixel
    return (getRed(pix) + getBlue(pix) + getGreen(pix))/3

def meanLuminosity(y):
# @param row : Int
    pixelsLumen = []
    rowLenght = len(y)
    for x in range(0, rowLenght):
        pix = getPixel(x, y)
        pixelsLumen.append(luminosity(pix))
    return sum(pixelsLumen) / rowLenght

def checkLuminosity(pict):
# @param pict : Picture
    mean = []
    for y in range(0, getHeight(pict)):
        meanRowLuminosity = meanLuminosity(y)
        if len(mean) == 0:
            mean.append(meanRowLuminosity)
        else:
            if meanRowLuminosity not in mean:
                return False
    return True

def prova1Problem8():
    print("#### PROBLEMA 8 ####")
    pict = makeEmptyPicture(30, 30, black)
    print(checkLuminosity(pict))

    for x in range(0, getWidth(pict)):
        pix = getPixel(x, 10)
        setColor(pix, white)
    print(checkLuminosity(pict))
#prova1Problem8()






""" PROBLEMA 9 """
def prova1Problema9a():
    print("#### PROBLEMA 9a ####")
    def start():
        a = 0.5
        F(a)
        print(a)

    def F(x):# x = '0.5'
        K()
        x = 8
        print(a+x)

    def K():
        global a
        a=4
    start() # 12, 0.5

def prova1Problema9b():
    print("#### PROBLEMA 9b ####")
    def start():
        a = 0.5
        F(a)
        print(a)

    def F(x):
        K()
        x = 8
        print(a+x)

    def K():
        #global a
        a=4
    start() # 8.3, 0.5

a = 0.3
#prova1Problema9a()
a = 0.3
#prova1Problema9b()



""" PROBLEMA 10 """
"""
# TODO:
"""



""" PROBLEMA 11 """
#dict = {[0,0]:1, [0,1]:2, [0,3]:3}
#x = dict[[0,1]]
#print (x)
# va in errore perchè le chiavi devono essere tipi di dato unmutable come stringhe, interi, tuple ...




""" PROBLEMA 12 """
def isPalindrome(s):
# @ param s : Str
    lenght = len(s)
    if lenght <= 1:
        return True
    elif s[0] in s[-1]: # aggiro l'operatore "=="
        return isPalindrome(s[1:-1])
    else:
        return False

def prova1Problem12():
    print("#### PROBLEMA 12 ####")
    print("La parola 'abcba' è palindroma", isPalindrome("abcba"))
    print("La parola 'ossesso' è palindroma", isPalindrome("ossesso"))
    print("La parola 'prova' è palindroma", isPalindrome("prova"))
    print("La parola 'ossesso' è palindroma", isPalindrome("osso"))
#prova1Problem12()




""" PROBLEMA 13 """
def countDigit(s, k, counter):
# @param s = Str
# @param k : Int
# @param counter : int
# @return bool
    if len(s) == 0:
        return counter == k
    else:
        if s[0].isdigit():
            counter = counter + 1
        return countDigit(s[1:], k, counter)


def prova1Problem13():
    print("#### PROBLEMA 13 ####")
    print(countDigit("12abb34cd67?^._", 6, 0))
    print(countDigit("12abb34cd67?^._", 7, 0))
    print(countDigit("12abb34cd67?^._", 5, 0))
#prova1Problem13()






""" PROBLEMA 14 """
class Veicolo:

    def __init__(self, passegeri, ruote):
        # @param passegeri : Int
        # @param ruote : Int
        self.passengers = passegeri
        self.wheels = ruote

    def getPassengers(self):
    # @return Int
        return self.passengers

    def getWheels(self):
    # @return Int
        return self.wheels

class VeicoloAMotore (Veicolo):

    def __init__(self, passegeri, ruote, potenzaDelMotore):
    # @param passegeri : Int
    # @param ruote : Int
    # @param potenzaDelMotore : Int
        super().__init__(passegeri, ruote)
        self.enginePower = potenzaDelMotore

    def getEnginePower(self):
    # @return Int
        return self.enginePower

    def increasePower(self, increaseRate):
    # @param increaseRate : Int
        self.enginePower = self.enginePower * increaseRate

def prova1Problem14():
    print("#### PROBLEMA 14 ####")
    veicolo = Veicolo(3, 4)
    print(veicolo.getPassengers())
    print(veicolo.getWheels())

    veicoloAMotore = VeicoloAMotore(2, 3, 50)
    print(veicoloAMotore.getPassengers())
    print(veicoloAMotore.getWheels())
    print(veicoloAMotore.getEnginePower())
    veicoloAMotore.increasePower(2.5)
    print(veicoloAMotore.getEnginePower())
prova1Problem14()




""" PROBLEMA 15 """
def checkSquareInsidePict(P, G, h, k):
# @param P : Picture
# @param G : Int
# @param h : Int
# @param k : Int
# @return bool
    for x in range(0, getWidth(P)-h):
        for y in range(0, getHeight(P)-k):
            if checkInsideRect(P, G, h, k, x, y):
                return True
    return False

def checkInsideRect(P, G, h, k, startX, startY):
# @param P : Picture
# @param G : Int
# @param h : Int
# @param k : Int
# @return bool
    for x in range(startX, startX + h):
        for y in range(0, startY, startY + k):
            pix = getPixel(P, x, y)
            greenComp = getGreen(pix)
            if greenComp < G:
                return False
    return True

def prova1Problem15():
    print("#### PROBLEMA 15 ####") 
    pict = makeEmptyPicture(50, 50, black)
    print(checkInsideRect(pict, 254, 10, 10))

    for x in range(0, 9):
        for y in range(0, 9):
            pix = getPixel(pict, x, y)
            setColor(pix, green)
    print(checkInsideRect(pict, 256, 10, 10))

    pict = makeEmptyPicture(50, 50, black)    
    for x in range(0, 10):
        for y in range(0, 10):
            pix = getPixel(pict, x, y)
            setColor(pix, green)
    print(checkInsideRect(pict, 254, 10, 10))
    print(checkInsideRect(pict, 255, 10, 10))

    pict = makeEmptyPicture(50, 50, black)    
    for x in range(0, 11):
        for y in range(0, 11):
            pix = getPixel(pict, x, y)
            setColor(pix, green)
    print(checkInsideRect(pict, 254, 10, 10))
    print(checkInsideRect(pict, 255, 10, 10))




""" PROBLEMA 16 """
def prova1Problem16a():
    print("#### PROBLEMA 16 ####")
    def start():
        R(a)
        print(a)

    def R(y):
        global a
        a = 10
        Q(y)
        y = a
        print(y)

    def Q(y):
        global a
        a = y
        print(a)
    start() # 20, 20, 20

def prova1Problem16b():
    print("#### PROBLEMA 16b ####")
    def start():
        R(a)
        print(a)

    def R(y):
        #global a
        a = 10
        Q(y)
        y = a
        print(y)

    def Q(y):
        #global a
        a = y
        print(a)
    start() # 20, 10, 20

a = 20
prova1Problem16a()
a = 20
prova1Problem16b()





""" PROBLEMA 17 """
def checkStringList(l):
# @param l : List
# @return Int
    listLen = len(l)
    if listLen == 0:
        return 0
    else:
        sLen = len(l[0])
        if sLen <= 1 or l[0][0] != l[0][1]:
            return checkStringList(l[1:])
        else: # l[0][0] == l[0][1]
            return 1 + checkStringList(l[1:])

def prova1problem17():
    print("#### PROBLEMA 17 ####")
    l = ["aba", "a", "hello", "prova"]
    print(checkStringList(l))
    l = ["a", "b", "c"]
    print(checkStringList(l))
    l = ["ab", "bc", "cd"]
    print(checkStringList(l))
    l = ["aa", "aba", "cc"]
    print(checkStringList(l))





""" PROBLEMA 18 """
def editTuple(t, i, v):
    newTuple = (,)
    for k in range(0, i):
        newTuple = newTuple + t[k]
    newTuple = newTuple + (v,) + t[i+1:]
    return newTuple

def prova1problem18():
    print("#### PROBLEMA 18 ####")
    myTuple = (1, 2, 3, 4, 5)
    i = 1
    v = 10
    newTule = editTuple(myTuple, i, v)
prova1problem18()




""" PROBLEMA 19 """
def prova1problem19a():
    def start():
        R(a)
        print(a)

    def R(x):
        Q()
        a = 'B'
        x = a
        print(x)

    def Q():
        global a
        a = 'b'
        print(a)
    start() # b B b

def prova1problem19b():
    def start():
        R(a)
        print(a)

    def R(x):
        Q()
        a = 'B'
        x = a
        print(x)

    def Q():
        #global a
        a = 'b'
        print(a)
    start() # b B A

a = 'A'
prova1problem19a()
a = 'A'
prova1problem19b()







""" PROBLEMA 20 """
def checkPictRowBlue(A, k):
# @param A : Picture
# @param k : Int
# @return bool
    assert getWidth(A)>=1 and getHeight(A)>=1
    for y in range(0, getHeight(A)):
        if not checkBlueComponent(A, y, k):
            return False
    return True

def checkBlueComponent(A, y, k):
# @param A : Pict
# @param y : Int
# @return bool
    max = 0
    min = 256
    for x in range(0, getWidth(A)):
        pix = getPixel(A, x, y)
        blueComp = getBlue(pix)
        if blueComp > max:
            max = blueComp
        if blueComp < min:
            min = blueComp
    return (max - min) < k
    
def prova1problem20():
    print("#### PROBLEMA 20 ####")
    pict = makeEmptyPicture(50, 50, blue)
    print(checkPictRowBlue(pict, 255))
    print(checkPictRowBlue(pict, 254))
prova1problem20()

