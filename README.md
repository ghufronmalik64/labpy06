## Nama         :   Ghufron Malik
## Kelas        :   TI.22.B2
## Mata kuliah  :   Bahasa Pemrograman


# Latihan 1
![img1](image/l1.png)

### Source Code
```py
import math

def a(x):
    return  x**2
a = lambda x : x**2
print(a(2))
def b(x, y):
        return math.sqrt(x**2 + y**2)

b = lambda x, y : x ** 2 + y ** 2
print(b(2, 2))
def c(*args):
        return sum(args)/len(args)

c = lambda *args : sum(args)/len(args)
print(c(1,2,3,4,5))
def d(s):
        return "".join(set(s))

d = lambda s: "".join(set(s))
print(d("TUGAS"))
```
### Output
![img2](image/l2.png)


# Tugas Praktikum

### Soal
Berikut adalah tampilan program sederhana dengan mengaplikasikan penggunaan fungsi yang akan menampilkan daftar nilai mahasiswa, dengan ketentuan:
• Fungsi tambah() untuk menambah data
• Fungsi tapilkan() untuk menampilkan data
• Fungsi hapus(nama) untuk menghapus data berdasarkan nama dan
• Fungsi ubah(nama) untuk mengubah data berdasarkan nama

### Program
![img2](image/0.png)
![img3](image/00.png)
![img4](image/000.png)

### Flowchart
![img5](image/1.png)

### Penjelasan
```py
a = {}

while True:
    t = input("\n(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar : ")
```

```py
    if t.lower() == 't':
        print("Tambah Data")
        nama = input("Nama\t\t: ")
        nim = int(input("NIM\t\t\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        a [nama] = nim, uts, uas, tugas, akhir
    ```