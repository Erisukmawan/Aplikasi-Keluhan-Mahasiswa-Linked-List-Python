import sys
import os
import json
from time import sleep
from prettytable import PrettyTable


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class KonserlList:
    def __init__(self):
        self.head = None
        self.list = []
                
    def menu(self):
        os.system('cls')
        print(F"{'='*50}")
        print(f"{'APLIKASI KELUHAN MAHASISWA UNIKOM': ^50}")
        print(F"{'='*50}")
        print("1. Tambah Keluhan Mahasiswa")
        print("2. Tampil Data Mahasiswa")
        print("3. Update Data Mahasiswa")
        print("4. Hapus Data Mahasiswa")
        print("5. Simpan data File Json")
        print("6. Buka File Json")
        print("7. Credit")
        print("8. Keluar Aplikasi")
        pilih = int(input("Masukkan pilihan anda : "))
        if pilih == 1 :
            self.tambahdata()
        elif pilih == 2 :
            self.display()
        elif pilih == 3 :
            self.editdata()
        elif pilih == 4 :
            self.hapusdata()
        elif pilih == 5 :
            self.simpanjson()
        elif pilih == 6 :
            self.bukajson()
        elif pilih == 7 :
            self.credit()
        elif pilih == 8:
            self.keluar()
        else:
            print("Menu Tidak Ada")
            self.menu()

    def isEmpty(self):
        return self.head is None
        
    def getLast(self):
        if self.isEmpty():
            return None
        else:
            bantu = self.head
            while bantu.next is not None:
                bantu = bantu.next
            return bantu

    def tambahdata(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU TAMBAH DATA': ^50}")
        print("="*50)
        sem = self.head
        if sem is None:
            nim = input ("Masukkan NIM Mahasiswa : ")
            nama = input("Masukkan Nama Mahasiswa : ").upper()
            print()
            print("Pilih Jenis Keluhan :")
            print("-"*40)
            print("1. FASILITAS SARANA DAN PRASARANA UNIKOM")
            print("2. KEUANGAN")
            print("3. PERKULIAHAN")
            print("-"*40)
            pilihan = int(input("Apa Jenis Keluhan Mahasiswa [1/2/3]: "))
            if(pilihan == 1):
                jenis = "FASILITAS SARANA DAN PRASARANA UNIKOM"
            elif(pilihan == 2):
                jenis = "KEUANGAN"
            elif (pilihan == 3):
                jenis = "PERKULIAHAN"
            else:
                print("menu tidak ada")
            isi = input("Apa Keluhan Mahasiswa : ")
            tanggal = input("Tanggal Keluhan format[01/01/2022]: ")
            temp_dic = {
                'nim':nim,
                'nama': nama,
                'jenis_keluhan': jenis,
                'isi_keluhan':isi,
                'tanggal':tanggal
                
            }
            add = Node(temp_dic)
            add.next = self.head
            self.head = add
            lista = self.list
            lista.append(temp_dic)

            print()
            print("Menyimpan data.....")
            sleep(2)
            print("Data Berhasil Disimpan")
            print()
            pilih = input("Apakah ingin menambahkan data kembali [Y/N]? ").upper()
            if pilih == 'Y':
                self.tambahdata()
            elif pilih == 'N':
                self.menu()
        else :
            nim = input ("Masukkan NIM Mahasiswa : ")
            nama = input("Masukkan Nama Mahasiswa : ").upper()
            print()
            print("Pilih Jenis Keluhan :")
            print("-"*40)
            print("1. FASILITAS SARANA DAN PRASARANA UNIKOM")
            print("2. KEUANGAN")
            print("3. PERKULIAHAN")
            print("-"*40)
            pilihan = int(input("Apa Jenis Keluhan Mahasiswa [1/2/3]: "))
            if(pilihan == 1):
                jenis = "FASILITAS SARANA DAN PRASARANA UNIKOM"
            elif(pilihan == 2):
                jenis = "KEUANGAN"
            elif (pilihan == 3):
                jenis = "PERKULIAHAN"
            else:
                print("menu tidak ada")
            isi = input("Apa Keluhan Mahasiswa : ")
            tanggal = input("Tanggal Keluhan format[01/01/2022]: ")
            temp_dic = {
                'nim':nim,
                'nama': nama,
                'jenis_keluhan': jenis,
                'isi_keluhan':isi,
                'tanggal':tanggal
                
            }
            add = Node(temp_dic)
            last = self.getLast()
            last.next = add
            lista = self.list
            lista.append(temp_dic)

            print()
            print("Menyimpan data.....")
            sleep(2)
            print("Data Berhasil Disimpan")
            
            print()
            pilih = input("Apakah ingin menambahkan data kembali [Y/N]? ").upper()
            if pilih == 'Y':
                self.tambahdata()
            elif pilih == 'N':
                self.menu()

    def display(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU TAMPIL DATA': ^50}")
        print("="*50)
        if self.isEmpty():
            print()
            print("Mencari data.....")
            sleep(2)
            print("Data : [Data Kosong]")
            print()
            pilih = input("Apakah ingin menambahkan data [Y/N]? ").upper()
            if pilih == 'Y':
                self.tambahdata()
            elif pilih == 'N':
                self.menu()
        else:
            print("Menampilkan data.....")
            sleep(2)
            indeks = self.head
            tabel = PrettyTable(["NIM","Nama","Jenis Keluhan","Isi Keluhan","Tanggal"])
            while indeks is not None :
                tabel.add_row([indeks.data["nim"],indeks.data["nama"],indeks.data["jenis_keluhan"],indeks.data["isi_keluhan"],indeks.data["tanggal"]])
                indeks = indeks.next
            print(tabel)
            
            print()
            input("kembali menu utama") 
            self.menu()

    def get(self, index):
        if self.isEmpty()or index<0:
            return None
        else:
            bantu = self.head
            posisi = 0
            while posisi<index:
                bantu = bantu.next
                posisi = posisi + 1
            return bantu

    def editdata(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU EDIT DATA': ^50}")
        print("="*50)
        if self.isEmpty() is None :
            print()
            print("Mencari data.....")
            sleep(2)
            print("Tidak dapat mengedit karena data kosong")
            print()
            input("kembali menu utama") 
            self.menu()
        else:
            # display
            print("Menampilkan data.....")
            sleep(2)
            indeks = self.head
            tabel = PrettyTable(["NIM","Nama","Jenis Keluhan","Isi Keluhan","Tanggal"])
            while indeks is not None :
                tabel.add_row([indeks.data["nim"],indeks.data["nama"],indeks.data["jenis_keluhan"],indeks.data["isi_keluhan"],indeks.data["tanggal"]])
                indeks = indeks.next
            print(tabel)

            da = self.list
            nim = input("Masukkan NIM anda : ")
            index_update=-1
            for a in range(0, len(da)): 
                if (da[a]['nim'] == nim):
                    print()
                    print("Mencari data.....")
                    sleep(2)
                    print("Data dengan NIM : ",nim, " Ditemukan")
                    print()
                    index_update = a
                    break
            if(index_update > -1): 
                nim = input ("Masukkan NIM Mahasiswa : ")
                nama = input("Masukkan Nama Mahasiswa : ").upper()
                print()
                print("Pilih Jenis Keluhan :")
                print("-"*40)
                print("1. FASILITAS SARANA DAN PRASARANA UNIKOM")
                print("2. KEUANGAN")
                print("3. PERKULIAHAN")
                print("-"*40)
                pilihan = int(input("Apa Jenis Keluhan Mahasiswa [1/2/3]: "))
                if(pilihan == 1):
                    jenis = "FASILITAS SARANA DAN PRASARANA UNIKOM"
                elif(pilihan == 2):
                    jenis = "KEUANGAN"
                elif (pilihan == 3):
                    jenis = "PERKULIAHAN"
                else:
                    print("menu tidak ada")
                isi = input("Apa Keluhan Mahasiswa : ")
                tanggal = input("Tanggal Keluhan format[01/01/2022]: ")
                temp_dic = {
                    'nim':nim,
                    'nama': nama,
                    'jenis_keluhan': jenis,
                    'isi_keluhan':isi,
                    'tanggal':tanggal
                    
                }
                da[index_update] = temp_dic
                nodeUpdate = self.get(index_update)
                if nodeUpdate is None:
                    print()
                    print("Memproses data.....")
                    sleep(2)
                    print("Data tidak ditemukan")
                else:
                    nodeUpdate.data = temp_dic 
                print()
                print("Menyimpan data.....")
                sleep(2)
                print("berhasil update data ") 
                print()

                print("Menampilkan data yang sudah diupdate")
                indeks = self.head
                tabel = PrettyTable(["NIM","Nama","Jenis Keluhan","Isi Keluhan","Tanggal"])
                while indeks is not None :
                    tabel.add_row([indeks.data["nim"],indeks.data["nama"],indeks.data["jenis_keluhan"],indeks.data["isi_keluhan"],indeks.data["tanggal"]])
                    indeks = indeks.next
                print(tabel)
            else : 
                print()
                print("Memproses data.....")
                sleep(2)
                print("Nama tidak ditemukan")

            print()
            pilih = input("Apakah ingin mengedit data kembali [Y/N]? ").upper()
            if pilih == 'Y':
                self.editdata()
            elif pilih == 'N':
                self.menu() 

    def hapusdata(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU HAPUS DATA': ^50}")
        print("="*50)
        if self.isEmpty() is None :
            print()
            print("Memproses data.....")
            sleep(2)
            print("Penghapusan gagal karena data kosong")
            sleep(5)
            return None
        else:
            print("Menampilkan data ......")
            indeks = self.head
            tabel = PrettyTable(["NIM","Nama","Jenis Keluhan","Isi Keluhan","Tanggal"])
            while indeks is not None :
                tabel.add_row([indeks.data["nim"],indeks.data["nama"],indeks.data["jenis_keluhan"],indeks.data["isi_keluhan"],indeks.data["tanggal"]])
                indeks = indeks.next
            print(tabel)
            da = self.list
            nim = input("Masukkan NIM anda : ")
            index_delete=-1
            for a in range(0, len(da)): 
                if (da[a]['nim'] == nim):
                    print()
                    print("Mencari data.....")
                    index_delete = a
                    break
            if(index_delete > -1):
                if index_delete==0:
                    first = self.head 
                    self.head = self.head.next
                    del first
                    del da[index_delete]
                else:
                    prevNode = self.get(index_delete - 1)
                    if prevNode is None:
                        print()
                        print("Meproses data.....")
                        sleep(2)
                        print("Data yang akan dihapus tidak ada")
                    else:
                        removedNode = prevNode.next
                        prevNode.next = removedNode.next
                        del removedNode
                        del da[index_delete]
                print()
                sleep(2)
                print("Data ",nim, "Telah di hapus")
                print("Menampilkan data yang sudah diupdate")
                indeks = self.head
                tabel = PrettyTable(["NIM","Nama","Jenis Keluhan","Isi Keluhan","Tanggal"])
                while indeks is not None :
                    tabel.add_row([indeks.data["nim"],indeks.data["nama"],indeks.data["jenis_keluhan"],indeks.data["isi_keluhan"],indeks.data["tanggal"]])
                    indeks = indeks.next
                print(tabel)

            else : 
                print()
                print("Mencari data.....")
                sleep(2)
                print("nama tidak ditemukan")
            print()
            pilih = input("Apakah ingin menghapus data kembali [Y/N]? ").upper()
            if pilih == 'Y':
                self.hapusdata()
            elif pilih == 'N':
                self.menu() 

    def simpanjson(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU SIMPAN FILE': ^50}")
        print("="*50)
        with open("file.json", 'w') as f:
            json.dump(self.list, f, indent=4)
        
        print("Sedang Menyimpan File Anda......")
        sleep(2)
        print("Menyimpan File Berhasil!")
        print()
        input("kembali menu utama")
        self.menu()

    def bukajson(self):
        os.system('cls')
        print("="*50)
        print(f"{'MENU BUKA FILE': ^50}")
        print("="*50)
        with open('file.json', 'r') as f:
            data = json.load(f)
        print("Memeriksa File Anda......")
        sleep(2)
        print(data)
        print()

        input("kembali menu utama")
        self.menu()
    def credit(self):
        os.system('cls')
        print("="*60)
        print(f"{'|': <15} {'DETAIL CREDIT': ^28} {'|': >15}")
        print("="*60)
        print(f"{'|': <15} {'': ^28} {'|': >15}")
        print(f"{'|': <15} {'PENCIPTA ERI SUKMAWAN': ^28} {'|': >15}")
        print(f"{'|': <14} {'NIM 10121139': ^28} {'|': >16}")
        print(f"{'|': <3} {'Aplikasi ini adalah Aplikasi Keluhan Mahasiswa UNIKOM': ^4} {'|': >2}")
        print(f"{'|': <6} {'Dibuat dengan Linked List - Single lInked List': ^11} {'|': >6}")
        print(f"{'|': <15} {'': ^28} {'|': >15}")
        print("="*60)
        input("kembali menu utama")
        self.menu()
    def keluar(self):
        print()
        print("Memproses Perintah.....")
        sleep(2)
        print("Terima Kasih, Selamat Tinggal")
        sys.exit(0)

tampil = KonserlList()
tampil.menu()