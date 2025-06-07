from flask import Blueprint, render_template, request, session, redirect, url_for
from app.models.pengeluaran import Pengeluaran

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    # Inisialisasi session jika belum ada
    if 'kategori_list' not in session:
        session['kategori_list'] = []
    if 'pengeluaran_list' not in session:
        session['pengeluaran_list'] = []
    if 'uang_total' not in session:
        session['uang_total'] = 0

    if request.method == 'POST':
        aksi = request.form.get('aksi')

        if aksi == 'submit_uang':
            session['uang_total'] = int(request.form.get('uang_total', 0))

        elif aksi == 'tambah_kategori':
            kategori = request.form.get('kategori')
            if kategori:
                session['kategori_list'].append(kategori)
                session.modified = True

        elif aksi == 'tambah_pengeluaran':
            pengeluaran = request.form.get('pengeluaran')
            if pengeluaran:
                try:
                    jumlah = int(pengeluaran)
                    session['pengeluaran_list'].append(jumlah)
                    session.modified = True
                except ValueError:
                    pass  # Tidak valid

        elif aksi == 'reset':
            session.clear()
            return redirect(url_for('main.index'))

        return redirect(url_for('main.index'))

    total_pengeluaran = sum(session.get('pengeluaran_list', []))
    sisa_uang = session.get('uang_total', 0) - total_pengeluaran

    return render_template(
        'index.html',
        kategori_list=session.get('kategori_list', []),
        pengeluaran_list=session.get('pengeluaran_list', []),
        uang_total=session.get('uang_total', 0),
        total_pengeluaran=total_pengeluaran,
        sisa_uang=sisa_uang
    )
