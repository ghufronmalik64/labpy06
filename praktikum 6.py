a = {}

while True:
    t = input("\n(T)ambah, (L)ihat, (U)bah, (H)apus, (C)ari, (K)eluar : ")

# MENAMBAHKAN DATA
    if t.lower() == 't':
        print("Tambah Data")
        nama = input("Nama\t\t: ")
        nim = int(input("NIM\t\t\t: "))
        uts = int(input("Nilai UTS\t: "))
        uas = int(input("Nilai UAS\t: "))
        tugas = int(input("Nilai Tugas\t: "))
        akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
        a [nama] = nim, uts, uas, tugas, akhir

# MELIHAT DATA
    elif t.lower() == 'l':
        if a.items():
            print("="*78)
            print("|                            Daftar Nilai Mahasiswa                          |")
            print("="*78)
            i = 0
            for z in a.items():
                i += 1
                print("| {no:2d} | {0:15s} | {1:15d} | {2:5d} | {3:5d} | {4:7d} | {5:7.2f} |"
                      .format(z[0][:13], z[1][0], z[1][1], z[1][2], z[1][3], z[1][4], no=i))
                print("="*78)
        else:
            print("="*78)
            print("|                        Daftar nilai Mahasiswa                           |")
            print("="*78)
            print("|                         TIDAK ADA DATA !!!                              |")
            print("="*78)

# MENGUBAH DATA
    elif t.lower() == 'u':
        print("Ubah Data")
        nama = input("\tMasukkan Nama\t\t: ")
        if nama in a.keys():
            nim = int(input("\tNIM\t\t\t: "))
            uts = int(input("\tNilai UTS\t\t\t: "))
            uas = int(input("\tNilai UAS\t\t\t: "))
            tugas = int(input("\tNilai Tugas\t\t\t: "))
            akhir = tugas * 30/100 + uts * 35/100 + uas * 35/100
            a[nama] = nim, uts, uas, tugas, akhir
        else:
            print("Nama {0} tidak ditemukan".format(nama))

# MENGHAPUS DATA
    elif t.lower() == 'h':
        print("Hapus Data")
        nama = input("Masukkan Nama : ")
        if nama in a.keys():
            del a[nama]
        else:
             print("Nama {0} Tidak Ditemukan".format(nama))

# MENCARI DATA
    elif t.lower() == 'c':
        print("Cari Data[case-sensitive]")
        nama = input("Masukkan Nama : ")
        if nama in a.keys():
            print("="*73)
            print("|                             Daftar Mahasiswa                          |")
            print("="*73)
            print("| Nama            |       NIM       |  UTS  |  UAS  |  Tugas  |  Akhir  |")
            print("="*73)
            print("| {0:15s} | {1:15d} | {2:5} | {3:5d} | {4:7d} | {5:7.3f} |"
                    .format(nama, nim, uts, uas, tugas, akhir))
            print("="*73)
        else:
            print("Nama {0} Tidak Ditemukan".format(nama))

# OUT
    elif t.lower() == 'k':
        break
    else:
        print("PILIH MENU YANG TERSEDIA !!!")
