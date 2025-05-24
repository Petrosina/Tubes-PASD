# app.py
from flask import Flask, request, jsonify
from core import Transaksi, LaporanKeuangan, Pengingat
import datetime

app = Flask(__name__)
laporan = LaporanKeuangan()
pengingat = Pengingat()

@app.route("/api/transaksi", methods=["GET"])
def get_transaksi():
    return jsonify(laporan.get_transaksi())

@app.route("/api/transaksi", methods=["POST"])
def tambah_transaksi():
    data = request.json
    try:
        t = Transaksi(
            jumlah=float(data["jumlah"]),
            kategori=data["kategori"],
            tanggal=datetime.datetime.strptime(data["tanggal"], "%Y-%m-%d").date()
        )
        laporan.tambah_transaksi(t)
        return jsonify({"message": "Transaksi ditambahkan"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/api/statistik", methods=["GET"])
def get_statistik():
    return jsonify(laporan.statistik())

@app.route("/api/rekomendasi", methods=["GET"])
def get_rekomendasi():
    return jsonify({"rekomendasi": laporan.rekomendasi()})

@app.route("/api/grafik", methods=["GET"])
def get_grafik_data():
    return jsonify(laporan.grafik_data())

@app.route("/api/pengingat", methods=["GET", "POST"])
def pengingat_handler():
    if request.method == "GET":
        return jsonify(pengingat.list_pengingat())
    else:
        data = request.json
        tanggal = datetime.datetime.strptime(data["tanggal"], "%Y-%m-%d").date()
        pengingat.atur_pengingat(data["jenis"], tanggal)
        return jsonify({"message": "Pengingat ditambahkan"}), 201

if __name__ == "__main__":
    app.run(debug=True)
