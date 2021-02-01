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
Data una lista di stringhe L e un intero n, scrivere una funzione ricorsiva che restituisce una nuova lista dove tutte le stringhe di lunghezza n sono maiuscole
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


def string_list_to_upper_1(L, n):
    # @param L : list
    # @param n : Int
    # @return list
    new_list = []
    for elem in L:
        if len(elem) == n:
            new_list.append(elem.toupper())
        else:
            new_list.append(elem)
    return new_list


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







"""PROBLEMA 3
"""
def tavola_pitagorica():
    custom_mat = []
    for x in range(1, 11):
        row = []
        for y in range(1, 11):
            row.append(x * y)
        custom_mat.append(row)

    return custom_mat


def problem3():
    print("### PROBLEM 3 ###")
    display_matrix(tavola_pitagorica())






"""PROBLEMA 4
"""
def count_zeros(mat):
    # @param mat : Matrix
    # @return Int
    counter = 0
    for y in range(0, len(mat)):
        for x in range(0, len(mat[0])):
            if mat[x][y] == 0:
                counter = counter + 1
    return counter


def problem4():
    print("### PROBLEM 4 ###")
    mat = random_matrix_generator(10, 10)
    display_matrix(mat)
    print(count_zeros(mat))






""" PROBLEM 5
Memorizzare in un array bidimensionale 5x5 tutti zeri tranne nelle celle della diagonale principale dove memorizzare 0
"""
def diagonal_matrix():
    mat = []
    for y in range(0, 5):
        row = []
        for x in range(0, 5):
            if x == y:
                row.append(1)
            else:
                row.append(0)
        mat.append(row)
    return mat


def problem5():
    print("### PROBLEM 5 ###")
    display_matrix(diagonal_matrix())







""" PROBLEM 6
"""
cmat = [
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [3, 3, 3, 3, 3, 3],
    [2, 2, 2, 2, 2, 2],
    [1, 1, 1, 1, 1, 1],
]

def palindrome_matrow_sums(mat):
    # @param mat : Matrix
    for x in range(0, round(len(mat) / 2)):
        upper_row_sum = sum(mat[x])
        bottom_row_sum = sum(mat[-x - 1])
        if upper_row_sum != bottom_row_sum:
            return False
    return True

def problem6():
    print("### PROBLEM 6 ###")
    print(palindrome_matrow_sums(cmat))


# recursive
def r_palindrome_matrow_sums(mat):
    # @param mat : Matrix
    if len(mat) == 0:
        return True
    elif len(mat) == 1:
        return False
    else:
        if sum(mat[0]) == sum(mat[-1]):
            return r_palindrome_matrow_sums(mat[1:-1])
        else:
            return False

def problem6_r():
    print("### PROBLEM 6 R ###")
    print(r_palindrome_matrow_sums(cmat))






""" PROBLEM 7
"""
def get_column(mat, col):
    # @param mat : Matrix
    # @param col : Int
    # @return list
    column = []
    for x in range(0, len(mat)):
        column.append(mat[x][col])
    return column


def get_highest_matindex(mat):
    # @param mat : Matrix
    # @return Int
    # rows
    higher_row_index = -1
    higher_row_value = -1
    i = 0
    while i < len(mat):
        current_sum = sum(mat[i])
        if current_sum > higher_row_value:
            higher_row_value = current_sum
            higher_row_index = i
        i = i + 1

    # columns
    higher_col_index = -1
    higher_col_value = -1
    j = 0
    while j < len(mat[0]):
        current_sum = sum(get_column(mat, j))
        if current_sum > higher_col_value:
            higher_col_value = current_sum
            higher_col_index = j
        j = j + 1
    return higher_col_index, higher_row_index


def problem7():
    print("### PROBLEM 7 ###")
    mat = random_matrix_generator(4, 4)
    display_matrix(mat)
    print(get_highest_matindex(mat))






""" PROBLEM 8
"""
def mat_cells_in_range(mat, n, m):
    # @param n : Int
    # @param m : Int
    for y in range(0, len(mat)):
        for x in range(0, len(mat[0])):
            elem = mat[x][y]
            if not (elem >= n and elem <= m):
                return False
    return True
def problem8():
    print("### PROBLEM 8 ###")
    mat = random_matrix_generator(5, 5)
    display_matrix(mat)
    print(mat_cells_in_range(mat, 0, 10))






""" ### MAIN ### """
def main():
    problem1()
    # --
    problem2()
    # --
    problem3()
    # --
    problem4()
    # --
    problem5()
    # --
    problem6()
    # --
    problem6_r()
    # --
    problem7()
    # --
    problem8()
main()
