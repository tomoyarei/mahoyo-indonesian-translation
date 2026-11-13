# Mahoyo Indonesian Translation Mod

Mod terjemahan Bahasa Indonesia untuk **Witch on the Holy Night**.

Mod ini dibuat oleh **Tomoya Rei** dan mencakup:

- Dialog Bahasa Indonesia yang telah disesuaikan agar lebih natural.
- Penyesuaian narasi dan gaya bicara karakter.
- Watermark pada gambar judul mod.
- Installer dengan fitur pencadangan dan pemulihan file game.

## Unduh

Versi terbaru dapat diunduh dari halaman
[Releases](https://github.com/tomoyarei/mahoyo-indonesian-translation/releases).

[Unduh installer terbaru](https://github.com/tomoyarei/mahoyo-indonesian-translation/releases/latest)

## Persyaratan

- Witch on the Holy Night versi PC yang sudah terpasang.
- Windows 10 atau Windows 11.
- Hak akses untuk menulis ke folder instalasi game.

## Cara Memasang

1. Unduh `TomoyaReiModInstaller.exe` dari bagian **Releases**.
2. Jalankan installer.
3. Pilih folder instalasi game.
4. Klik tombol pemasangan mod.
5. Tunggu sampai muncul pesan bahwa pemasangan berhasil.
6. Jalankan game seperti biasa.

Installer akan mencadangkan file game sebelum menggantinya. Jangan hapus file backup jika masih ingin memulihkan versi asli.

## Verifikasi Installer

Installer resmi tersedia di halaman [Releases](https://github.com/tomoyarei/mahoyo-indonesian-translation/releases/latest).

SHA-256 untuk `TomoyaReiModInstaller.exe` pada rilis `v1.0.0`:

```text
26E7CADE319C7CFFA04CC2D01D542B41823766CDCACEC39D90750CF86EBFED01
```

Di PowerShell, jalankan perintah berikut pada folder tempat installer berada:

```powershell
Get-FileHash .\TomoyaReiModInstaller.exe -Algorithm SHA256
```

Hasil `Hash` harus sama persis dengan nilai di atas.

## Cara Memulihkan

1. Jalankan kembali installer.
2. Pilih folder game yang sama.
3. Pilih opsi pemulihan atau penghapusan mod.
4. Tunggu sampai proses selesai.

Pemulihan mengembalikan file game dari backup yang dibuat saat pemasangan.

## Kendala Umum

- Tutup game dan Steam sebelum memasang atau memulihkan mod.
- Jika muncul `Permission denied`, jalankan installer sebagai administrator dan pastikan file game tidak sedang digunakan.
- Jika installer mendeteksi folder yang salah, pilih folder yang langsung berisi `data00000.hfa` dan `data00200.hfa`.
- Jangan menghapus file backup sebelum memastikan mod berjalan dengan baik.

## Catatan Penting

- Tutup game sebelum memasang atau memulihkan mod.
- Cadangkan file game secara manual jika diperlukan.
- Jangan mengubah nama file HFA selama proses berlangsung.
- Mod ini dibuat untuk penggunaan pribadi.
- Jangan mengunggah aset game asli atau file HFA lengkap ke repository publik.

## Kredit

Mod Bahasa Indonesia oleh **Tomoya Rei**.

Witch on the Holy Night adalah milik pemegang hak cipta masing-masing. Repository ini hanya berisi file mod dan alat pemasang yang dibuat untuk proyek ini.
