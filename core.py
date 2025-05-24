# core.py
import datetime
import csv
from collections import defaultdict
import matplotlib.pyplot as plt

class Transaksi:
    def __init__(self, jumlah, kategori, tanggal):
        self.jumlah = jumlah
        self.kategori = kategori
        self.tanggal = tanggal

    def to_dict(self):
        return {
            "jumlah": self.jumlah,
            "kategori": self.kategori,
            "tanggal": self.tanggal.strftime('%Y-%m-%d')
        }

class KategoriPengeluaran:
    def __init__(self):
        self.kategori = set()

    def tambah_kategori(self, nama):
        self.kategori.add(nama)

    def list_kategori(self):
        return list(self.kategori)

class LaporanKeuangan:
    def __init__(self):
        self.transaksi = []

    def tambah_transaksi(self, transaksi):
        self.transaksi.append(transaksi)

    def hapus_transaksi(self, index):
        del self.transaksi[index]

    def get_transaksi(self):
        return [t.to_dict() for t in self.transaksi]

    def statistik(self):
        if not self.transaksi:
            return {"max": 0, "min": 0, "rata_rata": 0}
        jumlah_list = [t.jumlah for t in self.transaksi]
        return {
            "max": max(jumlah_list),
            "min": min(jumlah_list),
            "rata_rata": sum(jumlah_list) / len(jumlah_list)
        }

    def rekomendasi(self):
        if not self.transaksi:
            return "Belum ada transaksi."
        rata2 = sum(t.jumlah for t in self.transaksi) / len(self.transaksi)
        return f"Usahakan pengeluaran harian tidak melebihi Rp{rata2:.2f}"

    def grafik_data(self):
        data = defaultdict(float)
        now = datetime.date.today()
        for t in self.transaksi:
            if t.tanggal.month == now.month and t.tanggal.year == now.year:
                data[t.kategori] += t.jumlah
        return dict(data)

class Pengingat:
    def __init__(self):
        self.pengingat = []

    def atur_pengingat(self, jenis_pengeluaran, tanggal):
        self.pengingat.append({"jenis": jenis_pengeluaran, "tanggal": tanggal.strftime('%Y-%m-%d')})

    def list_pengingat(self):
        return self.pengingat
