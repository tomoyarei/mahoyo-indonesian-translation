<div align="center">

# Mahoyo Indonesian Translation Mod

**Patch terjemahan fans Bahasa Indonesia untuk *Witch on the Holy Night* (Mahoyo) versi PC.**

![Platform](https://img.shields.io/badge/platform-Windows-blue)
![Bahasa](https://img.shields.io/badge/bahasa-Indonesia-red)
![Lisensi](https://img.shields.io/badge/lisensi-MIT-green)

<img width="1920" height="1080" alt="ss_title" src="https://github.com/user-attachments/assets/b0e521c3-7f79-4b84-8d59-642624d2aea3" />

</div>

---

## Tentang Proyek

Proyek ini merupakan terjemahan non-komersial buatan penggemar (*fan translation*) untuk visual novel **Witch on the Holy Night** (*Mahoutsukai no Yoru*). Patch dikemas dalam sebuah installer Windows sehingga proses pemasangan dan pemulihan dapat dilakukan tanpa konfigurasi manual.

Proyek ini tidak berafiliasi dengan pengembang maupun penerbit resmi. Diperlukan salinan game orisinal yang sah untuk menggunakan patch ini.

## Fitur

- Terjemahan naskah cerita utama, mencakup dialog dan narasi.
- Installer Windows mandiri, tanpa dependensi tambahan.
- Pencadangan otomatis file game sebelum dimodifikasi.
- Fitur pemulihan ke file asli dengan satu klik.

## Cakupan Terjemahan

| Komponen | Status |
|---|---|
| Dialog dan narasi cerita utama | Diterjemahkan |
| Menu, tombol, dan pengaturan | Belum diterjemahkan |
| Subtitle video | Belum diterjemahkan |
| Elemen antarmuka lainnya | Belum diterjemahkan |

<img width="1920" height="1080" alt="ingame_3" src="https://github.com/user-attachments/assets/5deb0a1e-fc8d-4651-87af-ea6cdd45e182" />

## Persyaratan

- Sistem operasi **Windows**.
- *Witch on the Holy Night* versi PC (Windows) yang sudah terpasang.

Installer tidak memerlukan Visual C++ Redistributable, .NET Framework, maupun Python secara terpisah.

## Panduan Pemasangan

1. Unduh `TomoyaReiModInstaller.exe` atau `TomoyaReiMahoyoIndo.zip` dari bagian **Releases**.
2. Pastikan Windows memiliki izin *Read/Write* ke folder instalasi game.
3. Jalankan installer.
4. Klik tombol **PASANG MOD**.

   <img width="619" height="288" alt="exe_1" src="https://github.com/user-attachments/assets/163955ee-397b-47e6-92f1-1ed786941d79" />

5. Pilih folder instalasi game yang berisi `data00000.hfa` dan `data00200.hfa`.

   <img width="944" height="592" alt="lokasi_game" src="https://github.com/user-attachments/assets/2607ebbe-9233-48f4-b86b-086586d2546c" />

6. Tunggu hingga muncul pesan bahwa pemasangan berhasil.

   <img width="264" height="208" alt="instal_mod" src="https://github.com/user-attachments/assets/a1cf33fc-9e25-4a7b-b16b-e38281fcdfbb" />

7. Jalankan game seperti biasa.

> [!NOTE]
> Installer akan mencadangkan file game sebelum menggantinya. File cadangan sebaiknya tidak dihapus apabila versi asli masih ingin dipulihkan.

## Panduan Pemulihan

1. Jalankan kembali installer.
2. Klik tombol **PULIHKAN FILE ASLI**.
3. Pilih folder instalasi game.
4. Tunggu hingga proses selesai.

   <img width="286" height="208" alt="restore_sukses" src="https://github.com/user-attachments/assets/e69fd3e5-fe9b-44d4-b122-a329f2c47c4b" />

Proses pemulihan mengembalikan file game dari cadangan yang dibuat saat pemasangan.

## Pemecahan Masalah

| Masalah | Solusi |
|---|---|
| Pemasangan atau pemulihan gagal | Tutup game dan Steam sebelum memulai proses. |
| Muncul pesan `Permission denied` | Jalankan installer sebagai administrator dan pastikan file game tidak sedang digunakan. |
| Installer mendeteksi folder yang salah | Pilih folder yang langsung berisi `data00000.hfa` dan `data00200.hfa`. |
| Mod tidak berjalan dengan baik | Jangan hapus file cadangan hingga mod dipastikan berfungsi normal. |

## Catatan Penting

- Tutup game sebelum memasang atau memulihkan mod.
- Lakukan pencadangan manual untuk file `data00000.hfa` dan `data00200.hfa` apabila diperlukan.
- Jangan mengubah nama file HFA selama proses berlangsung.
- Mod ini dibuat untuk penggunaan pribadi.
- Dilarang mengunggah aset game asli maupun file HFA lengkap ke repository publik.

## Kredit

- **Tomoya Rei**: terjemahan Bahasa Indonesia, installer, serta proses *packaging*.
- Terjemahan dibantu oleh AI (*AI-assisted translation*).

*Witch on the Holy Night* adalah milik pemegang hak ciptanya masing-masing. Repository ini hanya berisi file mod dan alat pemasang yang dibuat untuk proyek ini.

## Umpan Balik

Kritik, saran, dan laporan bug dapat disampaikan melalui Discord: **@tomoyarei** (Tomoya Rei #0574).

## Ucapan Terima Kasih

- [mahoyo_tools](https://github.com/loicfrance/mahoyo_tools): membaca dan mengonversi format aset Mahoyo.
- [HunexFileArchiveTool](https://github.com/LinkOFF7/HunexFileArchiveTool): mengekstrak dan membangun kembali arsip `.hfa`.
- [PyInstaller](https://github.com/pyinstaller/pyinstaller): membuat installer Windows dalam format `.exe`.
- ChatGPT dan Claude: alat bantu dalam penyusunan, pemeriksaan, dan penyempurnaan terjemahan.

## Lisensi

Proyek ini dilisensikan di bawah Lisensi MIT. Rincian lengkap tersedia pada berkas [LICENSE](LICENSE).
