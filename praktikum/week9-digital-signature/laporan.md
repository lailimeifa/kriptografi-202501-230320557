# Laporan Praktikum Kriptografi
Minggu ke-: X  
Topik: Digital Signature (RSA/DSA)
Nama: Laili Meifa Ayuningtias  
NIM: 2303020557  
Kelas: 5DSRA  

---

## 1. Tujuan
1. Mengimplementasikan tanda tangan digital menggunakan algoritma RSA/DSA.
2. Memverifikasi keaslian tanda tangan digital.
3. Menjelaskan manfaat tanda tangan digital dalam otentikasi pesan dan integritas data.

---

## 2. Dasar Teori
Digital Signature adalah mekanisme kriptografi yang digunakan untuk menjamin keaslian (authentication), keutuhan data (integrity), dan anti-penyangkalan (non-repudiation) pada suatu pesan atau dokumen digital. Berbeda dengan enkripsi yang berfokus pada kerahasiaan, tanda tangan digital bekerja dengan cara menandatangani hash dari pesan menggunakan private key pengirim, kemudian diverifikasi oleh penerima menggunakan public key yang sesuai. Jika hasil verifikasi cocok, maka pesan dipastikan tidak berubah dan benar berasal dari pemilik kunci tersebut.

Pada RSA Digital Signature, proses penandatanganan dilakukan dengan mengenkripsi nilai hash menggunakan private key RSA, sedangkan verifikasi dilakukan dengan public key. Keamanan RSA bergantung pada kesulitan faktorisasi bilangan prima besar. Sementara itu, DSA (Digital Signature Algorithm) menggunakan operasi matematika berbasis logaritma diskrit dan bilangan prima besar, serta menghasilkan tanda tangan yang lebih ringkas dan efisien untuk proses verifikasi, meskipun tidak digunakan untuk enkripsi data.

Digital Signature banyak diterapkan pada sistem keamanan modern seperti sertifikat digital, transaksi elektronik, distribusi perangkat lunak, dan komunikasi aman. Dengan mengombinasikan algoritma hash yang kuat dan manajemen kunci yang benar, digital signature menjadi komponen penting dalam menjaga kepercayaan dan keamanan data di lingkungan digital.

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
Pertanyaan 1: Diffie-Hellman memungkinkan pertukaran kunci di saluran publik karena kunci rahasia dihitung secara mandiri tanpa pernah dikirimkan langsung.

Pertanyaan 2: Kelemahan utama Diffie-Hellman murni adalah tidak adanya autentikasi sehingga rentan terhadap serangan Man-in-the-Middle (MITM).

Pertanyaan 3: Serangan MITM dapat dicegah dengan menambahkan autentikasi, seperti tanda tangan digital, sertifikat digital (PKI), atau mengombinasikannya dengan RSA/ECDSA.
---

## 8. Kesimpulan
Digital Signature menjamin keaslian, keutuhan, dan anti-penyangkalan data melalui mekanisme penandatanganan hash dengan private key, dengan ECDSA sebagai algoritma paling aman dan efisien saat ini dibanding RSA dan DSA. Sementara itu, Diffie-Hellman memungkinkan pertukaran kunci melalui saluran publik tetapi rentan terhadap serangan MITM jika tidak dilengkapi mekanisme autentikasi seperti tanda tangan digital atau sertifikat.

---

## 9. Daftar Pustaka
(Cantumkan referensi yang digunakan.  
Contoh:  
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  )

---

## 10. Commit Log

```
commit week9-digital signature
Author: Laili Meifa Ayuningtias <lailimeifa430@gmail.com>
Date:   2025-12-18

    week2-cryptosystem: implementasprogram python dengan digital signature dan laporan 
```
