# buku
books = [
    {"isbn":"9786237121144", "judul":"Kumpulan Solusi Pemrograman Python", "pengarang":"Budi Raharjo", "jumlah":6, "terpinjam":0},
    {"isbn":"9786231800718", "judul":"Dasar-Dasar Pengembangan Perangkat Lunak dan Gim Vol. 2", "pengarang":"Okta Purnawirawan", "jumlah":15, "terpinjam":0},
    {"isbn":"9786026163905", "judul":"Analisis dan Perancangan Sistem Informasi", "pengarang":"Adi Sulistyo Nugroho", "jumlah":2, "terpinjam":1},
    {"isbn":"9786022912828", "judul":"Animal Farm", "pengarang":"George Orwell", "jumlah":4, "terpinjam":0}
]

# data peminjaman
records = [
    {"isbn":"9786022912828", "status":"Selesai", "tanggal_pinjam":"2025-03-21", "tanggal_kembali":"2025-03-28"},
    {"isbn":"9786026163905", "status":"Belum", "tanggal_pinjam":"2025-07-22", "tanggal_kembali":""}
]

def bersih():
    import time
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_data():
    print("")

    for i in range(len(books)):
        print(i+1, "\t",  end=" ")
        print(books[i] ["isbn"],"\t", books[i]["judul"],"\t", books[i]["pengarang"],"\t", books[i]["jumlah"],"\t", books[i]["terpinjam"])
    
    print("=======================================================================================================================================================")
    print()

def tambah_data():
    print()
    print("tambahkan data disini")
    isbn = str(input("masukkan isbn: "))
    judul = str(input("masukkan judul: "))
    pengarang = str(input("masukkan pengarang: "))
    jumlah = int(input("masukkan jumlah: "))
    terpinjam = int(input("masukkan jumlah yang terpinjam: "))
    item = {"isbn":isbn, "judul":judul, "pengarang":pengarang, "jumlah":jumlah, "terpinjam":terpinjam}
    books.append(item)

    print("=======================================================================================================================================================")
    print()

def edit_data():
    print()

    tampilkan_data()

    index = int(input("pilih barang yang akan di ubah: ")) - 1

    books[index]["isbn"] = int(input("masukkan isbn buku yang baru: "))
    books[index]["judul"] = str(input("masukkan judul yang baru: "))
    books[index]["pengarang"] = str(input("masukkan pengarang yang baru: "))
    books[index]["jumlah"] = int(input("masukkan jumlah yang baru: "))
    books[index]["terpinjam"] = int(input("masukkan buku yang terpinjam yang baru: "))
    print("SELESAI")
    print("=======================================================================================================================================================")
    print()

def hapus_data():
    print()

    print("===HAPUS BUKU===")

    for i in range(len(books)):
        print(i+1, "\t",  end=" ")
        print(books[i] ["isbn"],"\t", books[i]["judul"],"\t", books[i]["pengarang"],"\t", books[i]["jumlah"],"\t", books[i]["terpinjam"])
        
    mana = int(input("pilih buku yang mana: ")) -1
    if mana >= 0 and mana < len(books): 
        del books[mana] 
            
    else:
        print("buku kamu ga ada, cihuyyyy")

    print("=======================================================================================================================================================")
    print()

def tampilkan_peminjaman():
    print()

    print("")

    for i in range(len(records)):
        print(i+1, "\t",  end=" ")
        print(records[i] ["isbn"],"\t", records[i]["status"],"\t", records[i]["tanggal_pinjam"],"\t", records[i]["tanggal_kembali"])
    
    print("=======================================================================================================================================================")
    print()

def tampilkan_belum():
    print("===== Menu tampilkan buku yang dipinjam namun belum kembali =====")
    j = 1
    for i in range(len(records)):
        if records[i]["status"] == "Belum":
                print(j, "\t", end=" ")
                print(records[i]["isbn"], "\t", records[i]["status"], "\t", records[i]["tanggal_pinjam"], "\t", records[i]["tanggal_kembali"], "\t")
                j += 1
            
        else:
            print("Semua buku sudah dikembalikan")
    print("==================================================================================================================================================================================")

def peminjaman():
    print("===== Menu pinjam buku =====")
    isbn = int(input("Masukkan isbn buku yang ingin ditambahkan : "))
    status = str(input("Masukkan status buku yang ada : "))
    tanggal_pinjam = str(input("Masukkan tanggal pinjam : "))
    tanggal_kembali = str(input("Masukkan tanggal kembali : "))
    peminjam = {"isbn":isbn, "status" : status, "tanggal_pinjam" : tanggal_pinjam, "tanggal_kembali" : tanggal_kembali}
    records.append(peminjam)
    print("==================================================================================================================================================================================")

def pengembalian():
    print("===== Menu pengembalian buku =====")
    tampilkan_peminjaman()

    index = int(input("Pilih buku yang ingin dikembalikan : ")) - 1

    records[index]["status"] = "Selesai"
    records[index]["tanggal_kembali"] = str(input("Masukkan tanggal kembali : "))
    print("==================================================================================================================================================================================")


def menu():
    print("---=== MENU ===---")
    print("[1] Tampilkan Data")
    print("[2] Tambah Data")
    print("[3] Edit Data")
    print("[4] Hapus Data")
    print("------------------")
    print("[5] Tampilkan Semua Peminjaman")
    print("[6] Tampilkan Peminjaman Belum Kembali")
    print("[7] Peminjaman")
    print("[8] Pengembalian")
    print("[X] Keluar")

    pilih = input("Masukkan pilihan menu (1-8 atau x): ")

    if pilih == "1":
        bersih()
        tampilkan_data()
        menu()
    
    elif pilih == "2":
        bersih()
        tambah_data()
        menu()
    
    elif pilih == "3":
        bersih()
        edit_data()
        menu()

    elif pilih == "4":
        bersih()
        hapus_data()
        menu()

    elif pilih == "5":
        bersih()
        tampilkan_peminjaman()
        menu()

    elif pilih == "6":
        bersih()
        tampilkan_belum()
        menu()
    
    elif pilih == "7":
        bersih()
        peminjaman()
        menu()

    elif pilih == "8":
        bersih()
        pengembalian()
        menu()

    elif pilih == "x" | "X":
        bersih()
        print("selesai")

menu()