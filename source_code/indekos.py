from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, harga_kos):
        super().__init__("Indekos")
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.harga_kos = harga_kos

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_harga_kos(self):
        return self.harga_kos

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nPenghuni : " + str(self.nama_penghuni) +"\nHarga Kos : " + str(self.harga_kos) + "\n"