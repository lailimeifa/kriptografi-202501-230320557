# Laporan Praktikum Kriptografi
Minggu ke-: XI
Topik: Public Key Infrastructure (PKI & Certificate Authority)

Nama: Laili Meifa Ayuningtias  
NIM: 230320557  
Kelas: 5DSRA  

---

## 1. Tujuan
1.  sertifikat digital sederhana.
2. Menjelaskan peran Certificate Authority (CA) dalam sistem PKI.
3. Mengevaluasi fungsi PKI dalam komunikasi aman (contoh: HTTPS, TLS).

---

## 2. Dasar Teori
Percobaan ini bertujuan untuk mensimulasikan proses pembuatan sertifikat digital menggunakan Python dan OpenSSL sebagai dasar penerapan keamanan berbasis Public Key Infrastructure (PKI). Melalui simulasi ini, ditunjukkan bagaimana pasangan kunci publik–privat dihasilkan, sertifikat ditandatangani, dan digunakan untuk membuktikan identitas suatu entitas dalam komunikasi digital.

Certificate Authority (CA) berperan sebagai pihak tepercaya yang bertugas memverifikasi identitas pemilik sertifikat sebelum menandatanganinya. Dengan adanya CA, pihak penerima dapat memastikan bahwa public key yang digunakan benar-benar milik pihak yang sah, sehingga mencegah pemalsuan identitas dan serangan Man-in-the-Middle.

PKI menyediakan kerangka kerja yang mengelola sertifikat digital, kunci kriptografi, dan mekanisme verifikasi kepercayaan dalam komunikasi aman. Melalui PKI, sistem seperti HTTPS, email terenkripsi, dan autentikasi jaringan dapat berjalan dengan aman karena adanya rantai kepercayaan yang dijamin oleh CA.

---

## 3. Alat dan Bahan
- Python 3.x  
- Visual Studio Code / editor lain  
- Git dan akun GitHub   

---

## 4. Langkah Percobaan
(Tuliskan langkah yang dilakukan sesuai instruksi.  
Contoh format:
1. Membuat file `caesar_cipher.py` di folder `praktikum/week2-cryptosystem/src/`.
2. Menyalin kode program dari panduan praktikum.
3. Menjalankan program dengan perintah `python caesar_cipher.py`.)

---

## 5. Source Code
(Salin kode program utama yang dibuat atau dimodifikasi.  
Gunakan blok kode:

```python
# contoh potongan kode
def encrypt(text, key):
    return ...
```
)

---

## 6. Hasil dan Pembahasan
(- Lampirkan screenshot hasil eksekusi program (taruh di folder `screenshots/`).  
- Berikan tabel atau ringkasan hasil uji jika diperlukan.  
- Jelaskan apakah hasil sesuai ekspektasi.  
- Bahas error (jika ada) dan solusinya. 

Hasil eksekusi program Caesar Cipher:

![Hasil Eksekusi](screenshots/output.png)
![Hasil Input](screenshots/input.png)
![Hasil Output](screenshots/output.png)
)

---

## 7. Jawaban Pertanyaan
MITM dalam komunikasi TLS/HTTPS?
jawab perta nyaan betikut jawab dengban jawaban singkat

Pertamyaan 1: Apa fungsi utama Certificate Authority (CA)?
CA berfungsi memverifikasi identitas pemilik sertifikat dan menandatangani sertifikat digital agar dapat dipercaya oleh pihak lain.
Pertanyaan 2: Mengapa self-signed certificate tidak cukup untuk sistem produksi?
Karena tidak diverifikasi oleh CA tepercaya, sehingga tidak menjamin keaslian identitas dan mudah disalahgunakan untuk serangan MITM.

Pertanyaan 3 : Bagaimana PKI mencegah serangan MITM dalam komunikasi TLS/HTTPS?
PKI mencegah MITM dengan memverifikasi sertifikat server melalui CA tepercaya, memastikan public key yang digunakan benar-benar milik server yang sah.
---

## 8. Kesimpulan
Certificate Authority dan PKI berperan penting dalam menjamin keaslian identitas dan keamanan komunikasi digital. Dengan verifikasi sertifikat oleh CA tepercaya, sistem seperti TLS/HTTPS dapat mencegah pemalsuan identitas dan serangan Man-in-the-Middle.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week10-pki
Author: Laili Meifa Ayuningtias <lailimeifa430@gmail.com>
Date:   2025-12-18

    week2-cryptosystem: implementasi PKI dan laporan 
```
