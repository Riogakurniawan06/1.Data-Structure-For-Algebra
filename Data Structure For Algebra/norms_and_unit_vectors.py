#Norms and Unit Vectors

#SOAL NO 1 (Matrix Tensors)

import numpy as np

# Membuat vektor kolom berukuran 3x1
vec_x = np.array([[15],
                  [7],
                  [31]])

print("Vektor x:\n", vec_x)

# Hitung L2 norm (panjang vektor)
norm_x = np.linalg.norm(vec_x)
print("Panjang (L2 norm) vektor x =", norm_x)


#SOAL NO 2 (Norms and Unit Vectors)

# Membuat vektor v
vec_v = np.array([3, 4])
print("Vektor v =", vec_v)

# Hitung L2 norm
norm_v = np.linalg.norm(vec_v)
print("Panjang v =", norm_v)

# Hitung unit vector
unit_v = vec_v / norm_v
print("Unit vector v =", unit_v)

# Verifikasi panjang unit vector
print("Panjang unit vector =", np.linalg.norm(unit_v))