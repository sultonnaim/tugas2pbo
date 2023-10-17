class Pegawai:
    def __init__(self, nama, id_pegawai):
        self.nama = nama
        self.id_pegawai = id_pegawai

    def hitung_gaji(self):
        pass

class PegawaiTetap(Pegawai):
    def __init__(self, nama, id_pegawai, gaji_pokok):
        super().__init__(nama, id_pegawai)
        self.gaji_pokok = gaji_pokok

    def hitung_gaji(self):
        return self.gaji_pokok

class PegawaiHarian(Pegawai):
    def __init__(self, nama, id_pegawai, tarif_per_jam, jam_kerja):
        super().__init__(nama, id_pegawai)
        self.tarif_per_jam = tarif_per_jam
        self.jam_kerja = jam_kerja

    def hitung_gaji(self):
        return self.tarif_per_jam * self.jam_kerja

class PegawaiKontrak(Pegawai):
    def __init__(self, nama, id_pegawai, durasi_kerja, upah_total):
        super().__init__(nama, id_pegawai)
        self.durasi_kerja = durasi_kerja
        self.upah_total = upah_total

    def hitung_gaji(self):
        return self.upah_total

# Fungsi untuk memasukkan data pegawai
def masukkan_data_pegawai():
    tipe_pegawai = input("Pilih jenis pegawai (tetap/harian/kontrak): ").lower()
    nama = input("Nama pegawai: ")
    id_pegawai = input("ID pegawai: ")

    if tipe_pegawai == "tetap":
        gaji_pokok = float(input("Gaji pokok: "))
        return PegawaiTetap(nama, id_pegawai, gaji_pokok)
    elif tipe_pegawai == "harian":
        tarif_per_jam = float(input("Tarif per jam: "))
        jam_kerja = float(input("Jam kerja: "))
        return PegawaiHarian(nama, id_pegawai, tarif_per_jam, jam_kerja)
    elif tipe_pegawai == "kontrak":
        durasi_kerja = float(input("Durasi kerja (bulan): "))
        upah_total = float(input("Upah total: "))
        return PegawaiKontrak(nama, id_pegawai, durasi_kerja, upah_total)
    else:
        print("Jenis pegawai tidak valid.")
        return None


daftar_pegawai = []

while True:
    opsi = input("Tambah pegawai (y/n): ").lower()
    if opsi != 'y':
        break
    pegawai = masukkan_data_pegawai()
    if pegawai:
        daftar_pegawai.append(pegawai)

print("Daftar Pegawai:")
for pegawai in daftar_pegawai:
    print(f"{pegawai.nama} ({pegawai.id_pegawai}): Gaji = {pegawai.hitung_gaji()}")
