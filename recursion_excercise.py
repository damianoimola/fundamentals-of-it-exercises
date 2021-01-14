# ----- PROBLEMI VARI ----- #
"""
Data una stringa s, ritornare in output la stringa senza vocali
"""
vowels = ["a", "e", "i", "o", "u"]
def delete_vowels(s):
# @param s : Str
# @return Str
    if len(s) == 0:
        return s
    else:
        if s[0] in vowels:
            return delete_vowels(s[1:])
        else:
            return s[0] + delete_vowels(s[1:])
print("# GENERICO 1 #")
print(delete_vowels("pippo"))
print(delete_vowels("pipp"))
print(delete_vowels("pippoo"))
print(delete_vowels("pippo0"))
print(delete_vowels("pippo?"))
print(delete_vowels("1234"))
print(delete_vowels("aeiou"))
print(delete_vowels("prova"))





""" 
"""
def return_digit(L):
# @param L : str
# @return list
    if len(L) == 0:
        return ""
    else:
        if L[0].isdigit():
            return L[0] + return_digit(L[1:])
        else:
            return return_digit(L[1:])

def count_digit(L):
# @param L : list T
# @return Int
    if len(L) == 0:
        return 0
    else:
        if L[0].isdigit():
            return 1 + count_digit(L[1:])
        else:
            return 0 + count_digit(L[1:])
print("# GENERICO 2 #")
print(return_digit("1A2b3C4d"))
print(count_digit("1A2b3C4d"))






# ----- PROBLEMI PROPOSTI DAI TUTOR ----- #

""" PROBLEMA 1a
Data una lista L di interi con possibili liste annidate al suo interno,
scrivere una funzione ricorsiva in Python che determina la somma di tutti i valori contenuti in L (anche quelli nelle liste annidate)
Per esempio, data la lista: L = [1, 5, [2, [1, 1], 4] ] la funzione deve restituire 14.
Suggerimento: usare la funzione type(obj) che ritorna il tipo di dato di obj
"""
def recursion1a(L):
# @param L : list
    if type(L) != int and len(L) == 0:
        return 0
    else:
        if type(L[0]) == int:
            return L[0] + recursion1a(L[1:])
        else:
            partial = 0
            for elem in L[0]:
                partial += recursion1a([elem])
            return partial + recursion1a(L[1:])

print("\n# PROBLEMA 1a #")
print(recursion1a([1,5,[2,[1,1],4]]))




""" PROBLEMA 1b
Data una lista L di interi con possibili liste annidate al suo interno,
scrivere una funzione ricorsiva in Python che determina la somma di tutti i valori contenuti in L (anche quelli nelle liste annidate)
Per esempio, data la lista: L = [1, 5, [2, [1, 1], 4] ] la funzione deve restituire 5.
Suggerimento: usare la funzione type(obj) che ritorna il tipo di dato di obj
"""
def recursion1b(L):
# @param L : list
    if len(L) == 0:
        return 0
    else:
        if type(L[0]) == int:
            return max(L[0], recursion1b(L[1:]))
        else:
            maxVal = 0
            for elem in L:
                actualMax = recursion1b(L[1:])
                if actualMax > maxVal:
                    maxVal = actualMax
            return max(maxVal, recursion1b(L[1:]))

print("\n# PROBLEMA 1b #")
print(recursion1b([1,5,[2,[1,1],4]]))





""" PROBLEMA 2
Scrivere una funzione ricorsiva in Python che, dati due interi positivi a e b, calcola a^b
"""
def recursion2(a, b):
# @param a : Int
# @param b : Int
# @return Int
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * recursion2(a, b-1)

print("\n# PROBLEMA 2 #")
print(recursion2(2,4))
print(recursion2(2,5))
print(recursion2(2,6))
print(recursion2(10,10))
print(recursion2(983864,0))





""" PROBLEMA 3
Scrivere una funzione ricorsiva in Python che, data una stringa S, la inverte.
"""
def recursion3(S):
# @param S : str
# @return Str
    if len(S) == 0:
        return ""
    else:
        return S[-1] + recursion3(S[:-1])

print("\n# PROBLEMA 3 #")
print(recursion3("pippo"))
print(recursion3("a"))
print(recursion3(""))
print(recursion3("prova"))






""" PROBLEMA 4
Scrivere una funzione ricorsiva in Python che, dato un intero positivo n, ritorna i coefficienti della riga n-esima del triangolo di Tartaglia. Ad esempio, per n= 4, ritorna [1, 3, 3, 1].
"""
def recursion4(n):
# @param n : Int
# @return Int
    print()

def recursion4bis(n, i=0):
# @param n : Int
# @return list
    if i == n or i == 0:
        return [1]
    else:
        tartaglia = [binomial_coefficient(n, i)]
        tartaglia.extend(recursion4bis(n, i+1))
        return tartaglia

def binomial_coefficient(n, k):
# @param n : Int
# @param k : Int
# @return Int
    return factor(n)/(factor(k) * factor(n-k))

def factor(n):
# @param n : Int
# @return n
    assert n>= 0, "Fattoriale di un numero negativo " + str(n)
    if n == 0:
        return 1
    else:
        return n * factor(n-1)

print("\n# PROBLEMA 4 #")
print(recursion4bis(1))
print(recursion4bis(2))
print(recursion4bis(3))
print(recursion4bis(4))
print(recursion4bis(5))
print(recursion4bis(6))





""" PROBLEMA 5
"""
class Iterator:
    def __init__(self, l):
    # @param index : Int
        self.index = 0
        self.list = l

    def hasNext(self):
        return ((len(self.list)-1) > self.index) != 0

    def hasPrevious(self):
        return ((len(self.list)-1) - self.index) != (len(self.list)-1)

    def next(self):
        if self.hasNext():
            self.index = self.index+1
            return self.list[self.index]
        else:
            return self.list[-1]

    def previous(self):
        if self.list.hasPrevious():
            self.index = self.index-1
            return self.list[self.index]
        else:
            return self.list[0]

    def add(self, elem):
    # @param elem : T
        self.list.insert(self.index+1, elem)

    def remove(self):
        removed = self.list[self.index+1]
        newList = self.list[:self.index] + self.list[self.index+1:]
        self.list = newList
        return removed

    def display(self):
        print(self.list)


def excercise5():
    print("# PROBLEMA 5 #")
    iterator = Iterator([1,2,3,4,5,6,7,8])
    print(iterator.hasNext())
    print(iterator.hasPrevious())
    iterator.display()
    iterator.add(99999)
    iterator.display()
    iterator.remove()
    iterator.display()
    
    print("---")
    iterator.next()
    iterator.next()
    print(iterator.hasNext())
    print(iterator.hasPrevious())
    iterator.display()
    iterator.add(99999)
    iterator.display()
    iterator.remove()
    iterator.display()

    print("---")
    iterator.next()
    iterator.next()
    print(iterator.hasNext())
    print(iterator.hasPrevious())
    iterator.display()
    iterator.add(99999)
    iterator.display()
    iterator.remove()
    iterator.display()
excercise5()

    



""" PROBLEMA 6
Scrivere una funzione Python che, data un’immagine P e un float
avg, si scorre la lista (usando l’Iterator definito nell’esercizio [5]) dei pixel di P e
ritorna vero se almeno un pixel ha la media delle componenti del proprio colore
strettamente maggiore di avg e falso altrimenti.
Suggerimento: la funzione getPixels(pict) ritorna una lista di pixel che può
essere passata all’Iterator.
"""
def problem6(P, avg):
# @param P : pict
# @param avg : float
# @return bool
    pixels = P.getPixels()
    iterator = Iterator(pixels)

    for pix in range(0, len(pixels)):
        elem = iterator.next()
        average = (getRed(elem) + getGreen(elem) + getBlue(elem))/3
        if average == avg:
            return True
    return False

pict = makeEmptyPicture(50, 50, white)
print(problem6(pict, 255))




""" PROBLEMA 7
Definire in Python una classe Knapsack (zaino) che prende come
parametro del costruttore un numero intero positivo C che indica la capacità
massima dello zaino. La classe ha come attributo una lista di Item (Item è a sua
volta una classe con un nome e un numero intero positivo che indica
l’occupazione nello zaino). E’ consentito l’inserimento di un Item nello zaino solo
se, aggiungendo l’occupazione dell’Item, non viene ecceduta la sua capacità
massima. Inoltre il Knapsack deve tenere traccia e ritornare su richiesta lo spazio
rimanente, il numero di elementi al suo interno, l’elemento con occupazione
massima e quello con occupazione minima.

"""
# TODO