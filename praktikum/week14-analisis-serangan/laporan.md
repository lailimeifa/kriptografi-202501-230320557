# Laporan Praktikum Kriptografi
Minggu ke-: 14  
Topik: Analisis Serangan Kriptografi
Nama: Laili Meifa Ayuningtias 
NIM: 230320557
Kelas: 5DSRA  

---

## 1. Tujuan
1. Mengidentifikasi jenis serangan pada sistem informasi nyata.
2. Mengevaluasi kelemahan algoritma kriptografi yang digunakan.
3. Memberikan rekomendasi algoritma kriptografi yang sesuai untuk perbaikan keamanan.

---

## 2. Dasar Teori
Serangan pada sistem informasi nyata merupakan ancaman yang dapat mengganggu kerahasiaan (confidentiality), integritas (integrity), dan ketersediaan (availability) data atau layanan. Salah satu jenis serangan yang paling umum adalah malware, seperti virus, worm, trojan, dan ransomware, yang bertujuan merusak sistem, mencuri data, atau mengenkripsi data agar tidak dapat diakses oleh pemiliknya. Serangan ini sering menyebar melalui email phishing, unduhan berbahaya, atau celah keamanan pada perangkat lunak.

Jenis serangan lain yang banyak terjadi adalah serangan jaringan, seperti Distributed Denial of Service (DDoS), yang bertujuan melumpuhkan layanan dengan membanjiri server menggunakan trafik palsu. Selain itu, terdapat serangan aplikasi web seperti SQL Injection dan Cross-Site Scripting (XSS), yang memanfaatkan kelemahan validasi input untuk mencuri atau memanipulasi data dalam basis data sistem informasi.

Di samping itu, serangan berbasis rekayasa sosial (social engineering) juga menjadi ancaman serius, karena memanfaatkan kelengahan manusia, bukan kelemahan teknis sistem. Contohnya adalah phishing, di mana penyerang menipu pengguna agar memberikan kredensial login atau informasi sensitif. Oleh karena itu, perlindungan sistem informasi tidak hanya bergantung pada teknologi keamanan, tetapi juga pada kesadaran dan perilaku pengguna.

---
## 4. Langkah Percobaan
1. Membuat laporan studi kasus analisis serangan sistem nyata.
2. Diskusi studi kasus sistem nyata
3. Commit Git dengan format week14-analisis-serangan.


---

## 5. Source Code
tidak ada

---
## 5. Source Code
Langkah 1 — Identifikasi Serangan
Contoh kasus yang dipilih adalah serangan brute force dan collision pada hash MD5. Vektor serangan dilakukan dengan mencoba berbagai kombinasi input untuk menghasilkan hash yang sama (collision) atau menemukan nilai asli dari hash. Kelemahan utama MD5 disebabkan oleh desain algoritma yang sudah tidak aman secara kriptografis dan rentan terhadap collision, sehingga penyerang dapat memalsukan data tanpa terdeteksi.

Langkah 2 — Evaluasi Kelemahan
Kelemahan pada kasus ini terutama terletak pada algoritma kriptografi itu sendiri, karena MD5 telah terbukti tidak lagi memenuhi standar keamanan modern. Selain itu, kelemahan juga sering diperparah oleh implementasi dan konfigurasi sistem, seperti penggunaan MD5 tanpa salt atau masih dipakai untuk penyimpanan password dan tanda tangan digital, yang seharusnya sudah digantikan oleh algoritma yang lebih aman seperti SHA-256 atau bcrypt.
Langkah 3 — Rekomendasi Solusi
Keamanan sistem dapat ditingkatkan dengan mengganti MD5 menjadi SHA-256/SHA-3 karena lebih tahan terhadap collision. Untuk kriptografi kunci publik, RSA lama sebaiknya diganti dengan ECC yang lebih efisien dan aman. Selain itu, password harus disimpan menggunakan bcrypt, scrypt, atau Argon2 agar lebih tahan terhadap serangan brute force dan dictionary.


---


## 7. Jawaban Pertanyaan  
- Pertanyaan 1: Mengapa banyak sistem lama masih rentan terhadap brute force atau dictionary attack?
Karena masih menggunakan algoritma usang, hash tanpa salt, serta kebijakan password yang lemah dan jarang diperbarui.
- Pertanyaan 2: Apa bedanya kelemahan algoritma dengan kelemahan implementasi?
Kelemahan algoritma berasal dari desain kriptografi yang tidak aman, sedangkan kelemahan implementasi terjadi karena kesalahan penerapan atau konfigurasi meskipun algoritmanya kuat.
- Pertanyaan 3: Bagaimana organisasi dapat memastikan sistem kriptografi mereka tetap aman di masa depan?
Dengan rutin memperbarui algoritma sesuai standar terbaru, menerapkan best practice keamanan, serta melakukan audit dan pengujian keamanan secara berkala.


---

## 8. Kesimpulan
Berdasarkan analisis studi kasus, penggunaan algoritma kriptografi yang sudah usang seperti MD5 dapat menimbulkan risiko keamanan yang serius pada sistem informasi. Kelemahan tidak hanya berasal dari algoritma, tetapi juga dari implementasi dan konfigurasi sistem yang kurang tepat. Oleh karena itu, penerapan algoritma kriptografi modern serta pembaruan dan audit keamanan secara berkala sangat penting untuk meningkatkan perlindungan sistem dari serangan.

---

## 9. Daftar Pustaka 
- Katz, J., & Lindell, Y. *Introduction to Modern Cryptography*.  
- Stallings, W. *Cryptography and Network Security*.  

---

## 10. Commit Log
```
commit week14-analisis-serangann
Author: Laili Meifa Ayuningtias <lailimeifa430@gmaio.com>
Date:   2026-01-21

    week14-analisis-serangann: Doskusi serangan keamanan dan laporan 
```
