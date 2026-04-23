# TRIANGLE-TUGAS

Proyek ini memuat penyelesaian kodingan bahasa Python untuk menggambar bangun segitiga 2D dan segitiga ilusi 3D (limas) dengan antarmuka grafis menggunakan pustaka bawaan `turtle`.

## 1. Segitiga 2D (`triangle.py`)

File ini bertugas membuat gambar segitiga sama sisi yang presisi di atas Canvas. Logika pemrograman di baliknya dilakukan dengan perputaran sudut dinamis:

- Komputer diinstruksikan untuk menjalankan fungsi *loop* perulangan `for _ in range(3):` (diseksekusi konstan sebanyak tiga kali berurutan).
- `t.forward(400)`: Pada setiap perulangan, ditarik garis lurus maju sepanjang 400 piksel dari posisi saat itu.
- `t.left(120)`: Garis tersebut kemudian dibelokan tajam 120 derajat ke arah kiri. Sudut 120 derajat dipakai karena keliling bentuk luarnya bila dijumlah akan setara dengan total rotasi (3 * 120 = 360).
- Sehingga secara otomatis, tiga tarikan garis itu saling mengiris satu dan lainnya menyusul menjadi bangunan tertutup bertitik sudut 60 derajat di dalamnya (segitiga sama sisi murni).

## 2. Segitiga 3D (`triangle_3d.py`)

File ini menampilkan proyeksi visual limas segitiga (bervolume 3D) namun direpresentasikan pada media Canvas 2D. Logika di baliknya memanfaatkan koordinat spasial (*Spatial X-Y coordinates*):

- **Pemetaan Diagonal Bidang 1 (Sisi Kiri)**: Menggunakan alur statis `goto()` dari titik pucuk sentral di atas `(0, 300)` lalu meluncur ke sudut minus kiri `(-200, -100)` dan berakhir meruncing di dasar tengah `(0, -180)` sebelum menutup ke atas. Area blok ini dicat penuh dengan warna biru terang (`blue`) sebagai parameter pencahayaan semu frontal.
- **Pemetaan Diagonal Bidang 2 (Sisi Kanan)**: Alur pantulan meniru sisi sebelumnya, diawali di titik yang persis sejajar namun dimiringkan berlawanan menjorok ke positif kanan bawah `(200, -100)`, memusat ke dasar yang sama. Area blok tertutup ini lalu dicerap warna biru tua/gelap (`darkblue`) untuk menduplikasi efek *shading* bayangan.
- Pertemuan gabungan dua balok warna ini dalam pandangan mata mengunci presisi ilusi sebuah bangun yang mencuat timbul menyerupai 3 dimensi padat.
