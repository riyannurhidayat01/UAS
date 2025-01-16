from flask import Flask, render_template, redirect, request, url_for
from DB_Operations import add_text, get_data, update_text, get_data_by_id, delete_text

app = Flask(__name__)

# Route untuk halaman utama
@app.route("/")
def website_pendidikan():
    data = get_data()  # Ambil semua data dari database
    return render_template('pendidikan.html', data=data)

# Route untuk halaman edit data berdasarkan ID
@app.route('/pendidikan_edit/<int:id>', methods=["GET", "POST"])
def edit_pendidikan(id):
    if request.method == "POST":
        # Update data jika metode POST
        nama_barang_jasa_value = request.form["nama_barang_jasa"]
        deskripsi_value = request.form["deskripsi"]
        updated = update_text(id, nama_barang_jasa_value, deskripsi_value)
        if updated:
            return redirect(url_for('website_pendidikan'))
        else:
            return "Failed to update data", 500
    else:
        # Ambil data untuk di-edit jika metode GET
        data = get_data_by_id(id)
        return render_template('pendidikan_edit.html', data=data)

# Route untuk menghapus data
@app.route('/pendidikan_delete/<int:id>')
def delete_pendidikan(id):
    deleted = delete_text(id)
    data = get_data()  # Ambil data terbaru setelah delete
    if deleted:
        return render_template('pendidikan.html', data=data)
    else:
        return "Failed to delete data", 500

# Route untuk menambahkan data baru
@app.route('/add_text', methods=["POST", "GET"])
def add_pendidikan():
    if request.method == "POST":
        # Tambahkan data baru jika metode POST
        nama_barang_jasa_value = request.form["nama_barang_jasa"]
        deskripsi_value = request.form["deskripsi"]
        add_new = add_text(nama_barang_jasa_value, deskripsi_value)
        if add_new:
            return redirect(url_for('website_pendidikan'))  # Kembali ke halaman utama
        else:
            return "Failed to add data", 500
    else:
        # Render halaman untuk menambahkan data
        return redirect(url_for('website_pendidikan'))

if __name__ == "__main__":
    app.run(debug=True)
