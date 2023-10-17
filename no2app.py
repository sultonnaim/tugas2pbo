from flask import Flask, render_template

app = Flask(__name__)

class Pegawai:
    def __init__(self, nama, nip, golongan, gaji):
        self.nama = nama
        self.nip = nip
        self.golongan = golongan
        self.gaji = gaji

    def perhitungan_gaji(self):
        return self.gaji

class PegawaiTetap(Pegawai):
    def __init__(self, nama, nip, golongan, gaji_pokok):
        super().__init__(nama, nip, golongan, gaji_pokok)

class PegawaiHarian(Pegawai):
    def __init__(self, nama, nip, golongan, jam_kerja, upah_per_jam):
        super().__init__(nama, nip, golongan, 0)  # Gaji awalnya 0
        self.jam_kerja = jam_kerja
        self.upah_per_jam = upah_per_jam

    def perhitungan_gaji(self):
        return self.jam_kerja * self.upah_per_jam

class PegawaiKontrak(Pegawai):
    def __init__(self, nama, nip, golongan, lama_kontrak, gaji_bulanan):
        super().__init__(nama, nip, golongan, 0)  # Gaji awalnya 0
        self.lama_kontrak = lama_kontrak
        self.gaji_bulanan = gaji_bulanan

    def perhitungan_gaji(self):
        return self.gaji_bulanan


@app.route('/')
def index():
    pegawai_tetap = PegawaiTetap("Mahya", "550913", "A", 5000000)
    pegawai_harian = PegawaiHarian("Tian", "67890", "B", 120, 5000)
    pegawai_kontrak = PegawaiKontrak("Rian", "54321", "C", 6, 2000000)
    return render_template('pegawai.html', pegawai_tetap=pegawai_tetap, pegawai_harian=pegawai_harian, pegawai_kontrak=pegawai_kontrak)

if __name__ == '__main__':
    app.run(debug=True)