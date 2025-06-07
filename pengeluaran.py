from datetime import datetime
import csv
import os

class Pengeluaran:
    def __init__(self, nama, jumlah, kategori, tanggal):
        self.nama = nama
        self.jumlah = jumlah
        self.kategori = kategori
        self.tanggal = datetime.strptime(tanggal, '%Y-%m-%d')

    def to_dict(self):
        return {
            'nama': self.nama,
            'jumlah': self.jumlah,
            'kategori': self.kategori,
            'tanggal': self.tanggal.strftime('%Y-%m-%d')
        }

def simpan_ke_csv(pengeluaran, file_path='data/pengeluaran.csv'):
    file_ada = os.path.exists(file_path)
    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['nama', 'jumlah', 'kategori', 'tanggal'])
        if not file_ada:
            writer.writeheader()
        writer.writerow(pengeluaran.to_dict())