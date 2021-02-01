"""
    --- PRACTICAL EXAM FUNCTIONS ---------
"""
import random

def random_row_generator(dimension):
# @param dimension : Int
# @return list
    row = []
    for x in range(0, dimension):
        row.append(random.randint(0, 10))
    return row

def random_matrix_generator(width, height):
# @param width : Int
# @param height : Int
# @return matrix
    custom_matrix = []
    for y in range(0, height):
        row = random_row_generator(width)
        custom_matrix.append(row)
    return custom_matrix

def display_matrix(mat):
# @param mat
    for y in range(0, len(mat)):
        print(mat[y])



""" PROBLEM 1
data una lista di stringhe L e un intero n, scrivere una funzione ricorsiva che restituisce una nuova lista dove tutte le stringhe di lunghezza n sono maiuscole
"""
def string_list_to_upper(L, n):
# @param L : list
# @param n : Int
# @return list
    if len(L) == 0:
        return L
    else:
        if len(L[0]) == n:
            return [L[0].upper()] + string_list_to_upper(L[1:], n)
        else:
            return [L[0]] + string_list_to_upper(L[1:], n)
def problem1():
    print("### PROBLEM 1 ###")
    print(string_list_to_upper(["abC", "a", "aei", "", "DEF", "AAAAAaaaaa"], 3))
    print(string_list_to_upper(["abc", "12re", "1rE", "", "std.Q", "AAAAAaaaaa"], 3))




""" PROBLEM 2
"""
def azzera_mul_k(A, k):
# @param A : matrix
# @param k : Int
# @return matrix
    for x in range(0, len(A)):
        for y in range(0, len(A[0])):
            if A[x][y] % k == 0:
                A[x][y] = 0
    return A

def problem2():
    print("### PROBLEM 2 ###")
    width = 10
    height = 2
    custom_matrix = random_matrix_generator(width, height)

    display_matrix(custom_matrix)
    display_matrix(azzera_mul_k(custom_matrix, 2))










def main():
    problem1()
    # --
    problem2()
main()