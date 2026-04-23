# Dokumentasi Code & Analogi Segitiga

Dokumen ini memuat penjelasan sederhana menggunakan analogi bagaimana kode Python (turtle) bisa menghasilkan bangun 2D dan 3D di layar monitor Anda.

---

## 1. Segitiga 2D (`triangle.py`)

**Analogi Sederhana:**

Bayangkan Anda sedang berdiri di tengah lapangan luas sambil memegang kapur lonceng yang menempel ke tanah. 
1. Anda berjalan lurus lurus ke depan sejauh 400 langkah. Jejak putih panjang pun tertinggal di tanah.
2. Setelah itu, Anda tidak boleh mundur. Anda memutar tubuh (belok serong) persis ke arah kiri sejauh **120 derajat**.
3. Dari posisi tersebut, Anda berjalan lurus lagi sejauh 400 langkah.
4. Terakhir, Anda berputar lagi ke kiri, lalu berjalan lurus lagi 400 langkah.

Tiba-tiba, Anda menyadari bahwa Anda sudah kembali ke titik tempat Anda memulainya! Garis jejak sepatu Anda di lapangan kini  membentuk **segitiga sama sisi yang sangat sempurna**. 

Itulah persisnya yang diinstruksikan oleh program ke *Turtle* (kura-kura/pena komputer) agar menggambar ke layar (*Canvas*).

---

## 2. Segitiga 3D (`triangle_3d.py`)

**Analogi Sederhana:**

Pernahkah Anda menggambar kubus, piramida, atau atap rumah di buku tulis? Kertasnya sangat datar (2 dimensi), tetapi gambar yang Anda buat "terlihat" memiliki ruang dan menonjol (3 dimensi). 

Pada program `triangle_3d.py`, kita melakukan hal yang murni serupa: **ilusi optik manusia saja**.

1. Kita menyuruh komputer menggambar bentuk layang-layang miring di sebelah **kiri**, lalu mengecatnya dengan warna biru cerah seolah-olah sisi tersebut sedang **terkena sinar lampu/matahari**.
2. Kemudian, kita menyambungkan bentuk layang-layang kedua tepat menempel di sebelah **kanannya**, namun dicat dengan warna biru gelap agar terlihat seperti sedang **berada di area bayangan tak tersinari**.

Otak dan mata kita secara insting saat melihat paduan sudut miring dan gradasi bayangan ini akan memprosesnya ("tertipu") sehingga melihatnya bukan lagi sebagai kumpulan garis di layar datar, melainkan sebuah bentuk limas / piramida 3D yang timbul dari dalam layar.
