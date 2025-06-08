
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Jawaban Proyek Ujian - UMKM, Koperasi, dan Bank Sampah</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 30px; background-color: #ffffff; }
        h1, h2, h3 { color: #333; }
        pre { background-color: #eee; padding: 10px; border-left: 4px solid #008080; overflow-x: auto; }
        code { font-family: "Courier New", Courier, monospace; }
        .output { background: #000; color: #0f0; padding: 10px; margin-top: 10px; white-space: pre-wrap; }
        .section { margin-bottom: 40px; }
    </style>
</head>
<body>
    <h1>📝 Jawaban Proyek Ujian - UMKM, Koperasi, dan Bank Sampah</h1>
    <p><strong>Nama Peserta:</strong> Farhan Fadillah </p>
    <p><strong>Batch:</strong> ETL Batch 9</p>
    <p><strong>No. Absen:</strong> 9.008.DB2025</p>
    <p><strong>Judul Proyek:</strong> Sistem Pengelolaan UMKM, Koperasi, dan Bank Sampah</p>

    <div class="section">
        <h2>📘 Pendahuluan</h2>
        <p>Proyek ini bertujuan membangun sistem manajemen sederhana menggunakan Python untuk membantu UMKM, koperasi desa, dan bank sampah agar lebih efisien dan berkelanjutan. Kami menggunakan konsep OOP, dictionary, list, loops, dan berbagai tools dari Chapter 1–15.</p>
    </div>

    <div class="section">
        <h2>🧩 Langkah-Langkah Penyelesaian</h2>

        <h3>Query 1: Class UMKMSystem</h3>
        <pre><code>class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000</code></pre>
        <p><strong>Penjelasan:</strong> Class ini adalah dasar dari sistem, menyimpan nama UMKM, daftar anggota, dan total dana pinjaman awal sebesar 50 juta rupiah.</p>

        <h3>Query 2: Method tambah_anggota</h3>
        <pre><code>def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
    self.anggota.append({
        "nama": nama_anggota,
        "pinjaman": jumlah_pinjaman
    })</code></pre>
    <p><strong>Penjelasan:</strong> Method ini menambahkan anggota baru ke dalam daftar, lengkap dengan nama dan jumlah pinjaman yang diajukan.</p>

        <h3>Query 3: Method Menghitung Pengembalian Pinjaman</h3>
        <pre><code>def hitung_pengembalian(self, nama_anggota, tahun):
    for anggota in self.anggota:
        if anggota["nama"] == nama_anggota:
            bunga = 0.05 * tahun * anggota["pinjaman"]
            return anggota["pinjaman"] + bunga
    return "Anggota tidak ditemukan."</code></pre>
    <p><strong>Penjelasan:</strong> Fungsi ini menghitung jumlah pengembalian pinjaman setelah periode tertentu, termasuk bunga 5% per tahun.</p>

        <h3>Query 4: Class Koperasi</h3>
        <pre><code>class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []</code></pre>
        <p><strong>Penjelasan:</strong> Kelas ini mewarisi UMKMSystem dan menambahkan fitur pencatatan transaksi jual dan beli untuk koperasi.</p>

        <h3>Query 5: Method catat_transaksi</h3>
        <pre><code>def catat_transaksi(self, nama_anggota, jenis, jumlah):
    self.transaksi.append({
        "nama": nama_anggota,
        "jenis": jenis,
        "jumlah": jumlah
    })</code></pre>
    <p><strong>Penjelasan:</strong> Method ini menyimpan data transaksi anggota berdasarkan nama, jenis (jual/beli), dan jumlahnya.</p>

        <h3>Query 6: Method hitung_keuntungan</h3>
        <pre><code>def hitung_keuntungan(self):
    total_jual = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "jual")
    total_beli = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "beli")
    return total_jual - total_beli</code></pre>
    <p><strong>Penjelasan:</strong> Fungsi ini menghitung total keuntungan koperasi dari selisih penjualan dan pembelian seluruh transaksi.</p>

        <h3>Query 7: Class BankSampah</h3>
        <pre><code>class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}</code></pre>
        <p><strong>Penjelasan:</strong> Kelas ini memperluas UMKMSystem dengan kemampuan menyimpan data jenis dan jumlah sampah dari tiap anggota.</p>

        <h3>Query 8: Method catat_sampah</h3>
        <pre><code>def catat_sampah(self, nama_anggota, jenis_sampah, jumlah_kg):
    if nama_anggota not in self.data_sampah:
        self.data_sampah[nama_anggota] = []
    self.data_sampah[nama_anggota].append({
        "jenis": jenis_sampah,
        "jumlah": jumlah_kg
    })</code></pre>
    <p><strong>Penjelasan:</strong> Fungsi ini mencatat jenis dan berat sampah (dalam kg) yang disetorkan oleh setiap anggota.</p>

        <h3>Query 9: Method hitung_nilai_tukar</h3>
        <pre><code>def hitung_nilai_tukar(self, nama_anggota):
    harga = {"plastik": 5000, "kertas": 2000, "logam": 8000}
    total = 0
    for item in self.data_sampah.get(nama_anggota, []):
        total += item["jumlah"] * harga.get(item["jenis"], 0)
    return total</code></pre>
    <p><strong>Penjelasan:</strong> Fungsi ini mengubah jumlah sampah menjadi nilai uang berdasarkan jenisnya (misalnya plastik = 5.000/kg).</p>

        <h3>Query 10: Method pesan_edukasi</h3>
        <pre><code>def pesan_edukasi(self, nama_anggota):
    total = sum(item["jumlah"] for item in self.data_sampah.get(nama_anggota, []))
    if total > 100:
        return "Luar biasa! Anda adalah pahlawan lingkungan desa!"
    elif total > 50:
        return "Kerja bagus! Terus tingkatkan kontribusi Anda!"
    elif total > 0:
        return "Terima kasih telah berkontribusi, mari kumpulkan lebih banyak!"
    else:
        return "Ayo mulai kumpulkan sampah dan jaga lingkungan kita!"</code></pre>
     <p><strong>Penjelasan:</strong> Memberikan pesan motivasi berdasarkan jumlah sampah yang dikumpulkan. Semakin banyak, semakin positif pesannya.</p>

        <h3>Query 11: Program Utama</h3>
        <pre><code>if __name__ == "__main__":
    nama_umkm = input("Masukkan nama UMKM: ")
    koperasi = Koperasi(nama_umkm)
    bank_sampah = BankSampah(nama_umkm)

    # Tambah anggota
    while True:
        nama = input("Nama anggota (atau 'selesai'): ")
        if nama.lower() == 'selesai':
            break
        pinjaman = int(input(f"Jumlah pinjaman untuk {nama}: "))
        koperasi.tambah_anggota(nama, pinjaman)
        bank_sampah.tambah_anggota(nama, pinjaman)

    # Tambah transaksi
    while True:
        nama = input("Nama anggota transaksi (atau 'selesai'): ")
        if nama.lower() == 'selesai':
            break
        jenis = input("Jenis transaksi (beli/jual): ")
        jumlah = int(input("Jumlah transaksi (Rp): "))
        koperasi.catat_transaksi(nama, jenis, jumlah)

    # Catat sampah
    while True:
        nama = input("Nama anggota sampah (atau 'selesai'): ")
        if nama.lower() == 'selesai':
            break
        jenis_sampah = input("Jenis sampah: ")
        jumlah_kg = float(input("Jumlah (kg): "))
        bank_sampah.catat_sampah(nama, jenis_sampah, jumlah_kg)

    # Output
    for anggota in koperasi.anggota:
        nama = anggota["nama"]
        pinjaman = anggota["pinjaman"]
        pengembalian = koperasi.hitung_pengembalian(nama, 1)
        nilai_sampah = bank_sampah.hitung_nilai_tukar(nama)
        pesan = bank_sampah.pesan_edukasi(nama)

        print(f"\nNama: {nama}")
        print(f"Pinjaman: Rp{pinjaman}")
        print(f"Pengembalian: Rp{int(pengembalian)}")
        print(f"Nilai Tukar Sampah: Rp{nilai_sampah}")
        print(f"Pesan Edukasi: {pesan}")

    print(f"\nTotal Keuntungan Koperasi: Rp{koperasi.hitung_keuntungan()}")</code></pre>
    <p><strong>Penjelasan:</strong> Program utama akan menjalankan seluruh alur — input data, simpan, dan menampilkan output. Semua kelas dan method sebelumnya digunakan di sini.</p>
    </div>

    <div class="section">
        <h2>🖥️ Contoh Output Terminal</h2>
        <div class="output">
UMKM: Tani Maju
Anggota: Budi
Pinjaman: 1000000
Pengembalian (1 tahun): Rp1050000
Nilai Tukar Sampah: Rp30000
Pesan Edukasi: Terima kasih telah berkontribusi, mari kumpulkan lebih banyak!

Total Keuntungan Koperasi: Rp250000
        </div>
    </div>

    <div class="section">
        <h2>📌 Catatan & Pembelajaran</h2>
        <p>Saya belajar bagaimana mengintegrasikan banyak konsep Python menjadi satu sistem terstruktur. Tantangan utama adalah menjaga agar data antar class tetap sinkron. Dengan sistem ini, saya merasa lebih siap membangun solusi nyata untuk masyarakat.</p>
    </div>

    <div class="section">
        <h2>🚫 Do’s & Don’ts</h2>
        <ul>
            <li>✅ Gunakan inheritance untuk menghindari duplikasi kode.</li>
            <li>✅ Gunakan dictionary untuk fleksibilitas penyimpanan data.</li>
            <li>❌ Jangan lupa konversi input dari `str` ke `int/float` sebelum perhitungan.</li>
            <li>❌ Jangan hardcode data — selalu gunakan input atau variable.</li>
        </ul>
    </div>
    <div class="section" style="margin-top: 40px;">
    <button onclick="window.open('https://etl-task-bank-sampah-farhan.streamlit.app/', '_blank')" 
        style="padding: 10px 20px; background-color: #008080; color: white; border: none; border-radius: 5px; cursor: pointer;">
        Buka Aplikasi
    </button>
    </div>
</body>
</html>

