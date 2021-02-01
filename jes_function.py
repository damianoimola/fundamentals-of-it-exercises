"""
    --- METHOD FOR JES ENVIRONMENT --------------
"""

""" PROBLEMA 1
Scrivere una funzione Python che, data un'immagine P e un float
avg, si scorre la lista (usando l'Iterator definito nell'esercizio [5]) dei pixel di P e
ritorna vero se almeno un pixel ha la media delle componenti del proprio colore
strettamente maggiore di avg e falso altrimenti.
Suggerimento: la funzione getPixels(pict) ritorna una lista di pixel che pu??
essere passata all'Iterator.
"""
def problem1(P, avg):
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
def exercise1():
    print("### PROBLEM 6 ###")
    pict = makeEmptyPicture(50, 50, white)
    print(problem6(pict, 255))

def main():
    exercise1()