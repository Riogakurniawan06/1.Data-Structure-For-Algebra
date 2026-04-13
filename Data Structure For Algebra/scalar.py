#Scalar

#SOAL NO 1 (SCALAR)

# Membuat variabel skalar
a = 25
b = 50

print("Nilai a =", a, "dengan tipe", type(a))
print("Nilai b =", b, "dengan tipe", type(b))

# Penjumlahan skalar
hasil1 = a + b
print("Hasil penjumlahan a+b =", hasil1)

# Skalar dengan bilangan desimal
a_float = 3.90
print("Nilai a_float =", a_float, "dengan tipe", type(a_float))

# Penjumlahan skalar desimal dengan b
hasil2 = a_float + b
print("Hasil penjumlahan a_float+b =", hasil2)


#SOAL NO 2 (SCALAR) (TENSORFLOW)

import tensorflow as tf

# Membuat variabel skalar TensorFlow
a_tf = tf.constant(25)
b_tf = tf.constant(50)

print("Tipe a_tf:", type(a_tf))
print("Tipe b_tf:", type(b_tf))

# Penjumlahan skalar TensorFlow
hasil3 = a_tf + b_tf
print("Hasil penjumlahan a_tf+b_tf =", hasil3)

# Skalar desimal dengan TensorFlow
a_float_tf = tf.constant(3.90)
hasil4 = a_float_tf + b_tf
print("Hasil penjumlahan a_float_tf+b_tf =", hasil4)

print("Tipe a_float_tf:", type(a_float_tf))


#SOAL NO 3 (SCALAR) (PYTORCH)

import torch

# Membuat variabel skalar PyTorch
a_pt = torch.tensor(25)
b_pt = torch.tensor(50)

print("a_pt =", a_pt, "dengan tipe", type(a_pt))
print("b_pt =", b_pt, "dengan tipe", type(b_pt))

# Penjumlahan skalar PyTorch
hasil5 = a_pt + b_pt
print("Hasil penjumlahan a_pt+b_pt =", hasil5)

# Skalar desimal dengan PyTorch
a_float_pt = torch.tensor(3.90)
hasil6 = a_float_pt + b_pt
print("Hasil penjumlahan a_float_pt+b_pt =", hasil6)

print("a_float_pt =", a_float_pt, "dengan tipe", type(a_float_pt))