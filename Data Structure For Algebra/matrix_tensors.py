# Matrix Tensors

#Soal No 1 (Matrix Tensors)

import numpy as np

# Membuat matriks 2x3
mat_np = np.array([[15, 7, 20],
                   [10, 6, 4]])

print("Matriks NumPy:\n", mat_np)

# Ukuran matriks
print("Ukuran matriks:", mat_np.shape)

# Elemen kolom pertama
print("Kolom pertama:", mat_np[:, 0])

# Elemen baris kedua
print("Baris kedua:", mat_np[1, :])


#Soal No 2 (Matrix Tensors) (PyTorch)

import torch

# Membuat tensor 2x3
mat_pt = torch.tensor([[15, 7, 20],
                       [10, 6, 4]])

print("Tensor PyTorch:\n", mat_pt)

# Ukuran tensor
print("Ukuran tensor:", mat_pt.shape)

# Elemen kolom pertama
print("Kolom pertama:", mat_pt[:, 0])

# Elemen baris kedua
print("Baris kedua:", mat_pt[1, :])