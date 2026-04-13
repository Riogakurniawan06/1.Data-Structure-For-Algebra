#Basis, Orthogonal, and Orthonormal Vectors

#SOAL NO 1 (Basis, Orthogonal, and Orthonormal Vectors)

import numpy as np

# Definisi vektor basis
i = np.array([1, 0])
j = np.array([0, 1])

print("Vektor i =", i)
print("Vektor j =", j)

# Hitung dot product
dp_ij = np.dot(i, j)
print("Dot product i·j =", dp_ij)

if dp_ij == 0:
    print("Kesimpulan: i dan j orthogonal (tegak lurus).")
else:
    print("Kesimpulan: i dan j tidak orthogonal.")


#SOAL NO 2 (Basis, Orthogonal, and Orthonormal Vectors)

# Definisi vektor lain
v = np.array([1, 2])
w = np.array([2, -1])

print("Vektor v =", v)
print("Vektor w =", w)

# Hitung dot product
dp_vw = np.dot(v, w)
print("Dot product v·w =", dp_vw)

if dp_vw == 0:
    print("Kesimpulan: v dan w orthogonal.")
else:
    print("Kesimpulan: v dan w tidak orthogonal.")