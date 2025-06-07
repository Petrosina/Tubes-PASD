import pandas as pd

class StatistikPengeluaran:
    def __init__(self, file_path='data/pengeluaran.csv'):
        self.data = pd.read_csv(file_path)

    def kategori_terbesar(self):
        return self.data.groupby('kategori')['jumlah'].sum().sort_values(ascending=False)

    def rata_rata_harian(self):
        self.data['tanggal'] = pd.to_datetime(self.data['tanggal'])
        return self.data.groupby(self.data['tanggal'].dt.date)['jumlah'].sum().mean()

    def estimasi_hari_bertahan(self, total_uang):
        rata_rata = self.rata_rata_harian()
        return round(total_uang / rata_rata, 2) if rata_rata else 0