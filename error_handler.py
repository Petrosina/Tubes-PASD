def validate_input(nama, jumlah, kategori, tanggal):
    if not nama or not kategori:
        raise ValueError("Nama dan kategori tidak boleh kosong.")
    if float(jumlah) < 0:
        raise ValueError("Jumlah pengeluaran tidak boleh negatif.")