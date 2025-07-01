def Gaussian_Lattice_Reduction(basis):
    v1 = basis[0]
    v2 = basis[1]
    if basis[1] > basis[0]:
        v1 = basis[1]
        v2 = basis[0]
    while True:
        if v1.norm() < v2.norm():
            v1, v2 = v2, v1 # obviously should swap if this is the case
        p = round(v1.dot_product(v2)/v2.dot_product(v2)) # projecting the taller vector onto the shorter & round to the spanned lattice
        if p == 0:
            break
        v1 -= p*v2 # reduce the taller vector
    
    return [v1, v2]
