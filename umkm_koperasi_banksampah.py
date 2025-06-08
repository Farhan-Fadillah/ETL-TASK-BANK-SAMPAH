import streamlit as st

# === CLASS DEFINITIONS ===

class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000

    def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
        self.anggota.append({
            "nama": nama_anggota,
            "pinjaman": jumlah_pinjaman
        })

    def hitung_pengembalian(self, nama_anggota, tahun):
        for anggota in self.anggota:
            if anggota["nama"] == nama_anggota:
                bunga = 0.05 * tahun * anggota["pinjaman"]
                return anggota["pinjaman"] + bunga
        return 0

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    def catat_transaksi(self, nama_anggota, jenis, jumlah):
        self.transaksi.append({
            "nama": nama_anggota,
            "jenis": jenis,
            "jumlah": jumlah
        })

    def hitung_keuntungan(self):
        total_jual = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "jual")
        total_beli = sum(t["jumlah"] for t in self.transaksi if t["jenis"] == "beli")
        return total_jual - total_beli

class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}

    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah_kg):
        if nama_anggota not in self.data_sampah:
            self.data_sampah[nama_anggota] = []
        self.data_sampah[nama_anggota].append({
            "jenis": jenis_sampah,
            "jumlah": jumlah_kg
        })

    def hitung_nilai_tukar(self, nama_anggota):
        harga_per_kg = {"plastik": 5000, "kertas": 2000, "logam": 8000}
        total = 0
        for item in self.data_sampah.get(nama_anggota, []):
            total += item["jumlah"] * harga_per_kg.get(item["jenis"], 0)
        return total

    def pesan_edukasi(self, nama_anggota):
        total_kg = sum(item["jumlah"] for item in self.data_sampah.get(nama_anggota, []))
        if total_kg > 100:
            return "Luar biasa! Anda adalah pahlawan lingkungan desa!"
        elif total_kg > 50:
            return "Kerja bagus! Terus tingkatkan kontribusi Anda!"
        elif total_kg > 0:
            return "Terima kasih telah berkontribusi, mari kumpulkan lebih banyak!"
        else:
            return "Ayo mulai kumpulkan sampah dan jaga lingkungan kita!"

# === STREAMLIT INTERFACE ===

st.title("Sistem Pengelolaan UMKM, Koperasi, dan Bank Sampah")

nama_umkm = st.text_input("Masukkan nama UMKM")

if nama_umkm:
    koperasi = Koperasi(nama_umkm)
    bank_sampah = BankSampah(nama_umkm)

    st.header("Tambah Anggota")
    with st.form("form_anggota"):
        nama_anggota = st.text_input("Nama anggota")
        pinjaman = st.number_input("Jumlah pinjaman", 0)
        submitted = st.form_submit_button("Tambah Anggota")
        if submitted:
            koperasi.tambah_anggota(nama_anggota, pinjaman)
            bank_sampah.tambah_anggota(nama_anggota, pinjaman)
            st.success(f"Anggota {nama_anggota} ditambahkan.")

    st.header("Transaksi Koperasi")
    with st.form("form_transaksi"):
        nama_transaksi = st.text_input("Nama anggota (transaksi)")
        jenis = st.selectbox("Jenis transaksi", ["beli", "jual"])
        jumlah_transaksi = st.number_input("Jumlah transaksi (Rp)", 0)
        submit_transaksi = st.form_submit_button("Catat Transaksi")
        if submit_transaksi:
            koperasi.catat_transaksi(nama_transaksi, jenis, jumlah_transaksi)
            st.success(f"Transaksi {jenis} oleh {nama_transaksi} dicatat.")

    st.header("Input Sampah")
    with st.form("form_sampah"):
        nama_sampah = st.text_input("Nama anggota (sampah)")
        jenis_sampah = st.selectbox("Jenis sampah", ["plastik", "kertas", "logam"])
        jumlah_kg = st.number_input("Jumlah (kg)", 0.0)
        submit_sampah = st.form_submit_button("Catat Sampah")
        if submit_sampah:
            bank_sampah.catat_sampah(nama_sampah, jenis_sampah, jumlah_kg)
            st.success(f"{jumlah_kg} kg {jenis_sampah} dicatat untuk {nama_sampah}.")

    st.header("Laporan UMKM")

    for anggota in koperasi.anggota:
        nama = anggota["nama"]
        pinjaman = anggota["pinjaman"]
        pengembalian = koperasi.hitung_pengembalian(nama, 1)
        nilai_tukar = bank_sampah.hitung_nilai_tukar(nama)
        pesan = bank_sampah.pesan_edukasi(nama)

        st.subheader(f"Anggota: {nama}")
        st.write(f"Pinjaman Awal: Rp{pinjaman}")
        st.write(f"Pengembalian (1 tahun): Rp{int(pengembalian)}")
        st.write(f"Nilai Tukar Sampah: Rp{int(nilai_tukar)}")
        st.write(f"Pesan Edukasi: {pesan}")

    st.success(f"Total Keuntungan Koperasi: Rp{koperasi.hitung_keuntungan()}")

st.markdown("---")
st.markdown("Made by Farhan Fadillah")