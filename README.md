# Mahoyo Indonesian Translation Mod

Mod terjemahan Bahasa Indonesia untuk **Witch on the Holy Night**.

## Cakupan Terjemahan

- Mod ini menerjemahkan naskah cerita utama, termasuk dialog dan narasi.
- Menu, tombol, pengaturan, subtitle video, serta elemen antarmuka lainnya belum diterjemahkan.

## Dukungan Sistem Operasi

- Installer ini hanya dapat dijalankan di Windows.

## Persyaratan

- Witch on the Holy Night versi PC Windows yang sudah terpasang.

Installer tidak memerlukan Visual C++ Redistributable, .NET Framework, atau Python secara terpisah.

## Cara Memasang

1. Unduh `TomoyaReiModInstaller.exe` dari bagian **Releases**.
2. Pastikan Windows memiliki izin Read/Write ke folder instalasi game.
3. Jalankan installer.
4. Klik tombol pemasangan mod.
5. Pilih folder instalasi game yang berisi `data00000.hfa` dan `data00200.hfa`.
6. Tunggu sampai muncul pesan bahwa pemasangan berhasil.
7. Jalankan game seperti biasa.

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
2. Pilih opsi pemulihan atau penghapusan mod.
3. Pilih folder game.
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

- Mod Bahasa Indonesia oleh **Tomoya Rei**.
- AI-assisted translation of Witch on the Holy Night.
- Installer dan proses packaging dibuat untuk proyek ini oleh **Tomoya Rei**.

Witch on the Holy Night adalah milik pemegang hak cipta masing-masing. Repository ini hanya berisi file mod dan alat pemasang yang dibuat untuk proyek ini.

## Acknowledgements

- [mahoyo_tools](https://github.com/loicfrance/mahoyo_tools), untuk membantu membaca dan mengonversi format aset Mahoyo.
- [HunexFileArchiveTool](https://github.com/LinkOFF7/HunexFileArchiveTool), untuk mengekstrak dan membangun kembali arsip `.hfa`.
- [PyInstaller](https://github.com/pyinstaller/pyinstaller), untuk membuat installer Windows dalam format `.exe`.
- - AI digunakan sebagai alat bantu dalam penyusunan, pemeriksaan, dan penyempurnaan terjemahan.

## License

This project is licensed under the MIT License. For more details, see the [LICENSE](LICENSE) file.
