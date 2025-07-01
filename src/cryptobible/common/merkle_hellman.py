from sage.all import *

def merkle(a : list, S : int):
    """
    given a = [a_i ... ], S = sum(a_i * x_i) 
    returns list [x_i ... ] or the entire lattice solved in case cant find

    Args :
        a (list) : 1D vector of ints
        S : sum

    """
    n = len(a)
    M = Matrix([a + [-S]] + [[1 if i == j else 0 for i in range(n+1)] for j in range(n)]).T
    L = M.LLL()
    for i in L:
        if i[0] == 0:
            return i[1:]
        else:
            print("trouble finding the correct vector...\ncheck manually")
            return L
