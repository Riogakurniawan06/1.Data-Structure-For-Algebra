#Exercises on Algebra Data Structures

#SOAL NO 1 (Exercises on Algebra Data Structures)

# selesaikan soal berikut
# What is the transpose of this vector?
# [25]
# [2]
# [-3]
# [-23]

import numpy as np

# Membuat vektor kolom
x = np.array([[25],
              [2],
              [-3],
              [-23]])

print("Vektor kolom x:\n", x)

# Transpose vektor
x_transpose = x.T
print("Transpose dari x adalah:\n", x_transpose)