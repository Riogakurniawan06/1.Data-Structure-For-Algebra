#Vectors and Vector Transposition

#SOAL NO 1 (VECTORS AND VECTOR TRANSPOSITION)

import numpy as np

# Membuat vektor kolom berukuran 3x1
vec_x = np.array([[10],
                  [15],
                  [20]])

print("Vektor x:\n", vec_x)

# Panjang vektor (jumlah elemen)
print("Jumlah elemen vektor x =", len(vec_x))

# Ukuran vektor
print("Ukuran vektor x =", vec_x.shape)

# Tipe data vektor
print("Tipe data vektor x =", type(vec_x))

# Akses elemen pertama
print("Elemen pertama =", vec_x[0])

# Tipe data elemen pertama
print("Tipe elemen pertama =", type(vec_x[0]))


#SOAL NO 2 (VECTORS AND VECTOR TRANSPOSITION)

# Transpose vektor x
vec_x_t = vec_x.T
print("Transpose vektor x:\n", vec_x_t)
print("Ukuran transpose =", vec_x_t.shape)

# Membuat vektor y
vec_y = np.array([[10],
                  [15],
                  [20]])
print("Vektor y:\n", vec_y)
print("Ukuran vektor y =", vec_y.shape)


#SOAL NO 3 (VECTORS AND VECTOR TRANSPOSITION) (TENSORFLOW)

import tensorflow as tf

# Membuat vektor dengan TensorFlow
vec_tf = tf.constant([[10],
                      [15],
                      [20]])

print("Vektor TensorFlow:\n", vec_tf)
print("Ukuran vektor TensorFlow =", vec_tf.shape)

vec_y_tf = tf.constant([[10],
                        [15],
                        [20]])

print("Vektor y_tf:\n", vec_y_tf)
print("Ukuran vektor y_tf =", vec_y_tf.shape)


#SOAL NO 4 (VECTORS AND VECTOR TRANSPOSITION) (PYTORCH)

import torch

# Membuat vektor dengan PyTorch
vec_pt = torch.tensor([[10],
                       [15],
                       [20]])

print("Vektor PyTorch:\n", vec_pt)
print("Ukuran vektor PyTorch =", vec_pt.shape)

vec_y_pt = torch.tensor([[10],
                         [15],
                         [20]])

print("Vektor y_pt:\n", vec_y_pt)
print("Ukuran vektor y_pt =", vec_y_pt.shape)