#Generic Tensor Notation

#SOAL NO 1 (Generic Tensor Notation)

# jelaskan tentang perintah ini
# images_pt = torch.zeros([32, 28, 28, 3])

import torch

# Membuat tensor gambar kosong
images = torch.zeros((32, 28, 28, 3))

print("Ukuran tensor:", images.shape)
print("Contoh isi tensor:\n", images[0])


# Penjelasan

#1. import torch
Mengimpor library PyTorch agar kita bisa membuat dan mengolah tensor.

#2. images = torch.zeros((32, 28, 28, 3))
Membuat tensor berisi angka nol dengan dimensi (32, 28, 28, 3).
Artinya:
32 → jumlah data (batch size), biasanya jumlah gambar dalam satu batch.
28 → tinggi gambar (height).
28 → lebar gambar (width).
3 → channel warna (RGB).
Jadi tensor ini mewakili 32 gambar kosong berukuran 28×28 piksel dengan 3 channel warna.
Karena semua nilainya nol, gambar yang dihasilkan berwarna hitam.

#3. print("Ukuran tensor:", images.shape)
Menampilkan ukuran tensor, yaitu (32, 28, 28, 3).
Ini berguna untuk memastikan dimensi sesuai dengan yang kita inginkan.

#4. print("Contoh isi tensor (gambar pertama):\n", images[0])
Menampilkan isi tensor untuk gambar pertama (index 0).
Hasilnya adalah matriks 28×28×3 yang semuanya bernilai 0.