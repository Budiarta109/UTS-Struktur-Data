## UTS-Struktur-Data

# 1.Rumusan Masalah
1.	Bagaimana struktur data Queue dengan prinsip FIFO (First In First Out) dapat diterapkan untuk mengelola antrian kendaraan pada sistem parkir agar proses masuk dan keluar berjalan         secara terurut dan adil?
2.	Bagaimana implementasi Queue menggunakan collections.deque di Python mampu memberikan efisiensi waktu O(1) pada operasi enqueue dan dequeue dibandingkan penggunaan list biasa?
3.	Bagaimana sistem parkir berbasis Queue dapat menyelesaikan permasalahan nyata seperti pengelolaan kapasitas slot yang terbatas, pencegahan duplikasi nomor plat, dan perhitungan          durasi serta biaya parkir secara otomatis?
# 2.Solusi yang Ditawarkan
Sistem yang dibuat menggunakan struktur data Queue untuk mensimulasikan antrian kendaraan. Kendaraan yang masuk pertama kali akan keluar pertama kali (FIFO). Sistem menyediakan pengecekan kapasitas secara real-time, pencegahan duplikat plat, perhitungan durasi dan biaya otomatis, serta penyimpanan riwayat parkir.

# 3.Landasan Teori
Struktur data adalah cara mengorganisasikan, menyimpan, dan mengelola data agar dapat diakses dan dimanipulasi dengan efisien. Struktur data linier seperti array, linked list, stack, dan queue banyak digunakan dalam berbagai aplikasi.
Queue merupakan struktur data linier yang menerapkan prinsip FIFO (First In First Out). Elemen yang pertama masuk akan menjadi elemen pertama yang keluar. Operasi utama Queue adalah enqueue (menambah di belakang) dan dequeue (menghapus di depan). Sementara itu, Stack menggunakan prinsip LIFO (Last In First Out).
Queue dapat diimplementasikan dengan array (menggunakan circular queue) atau linked list. Dalam Python, struktur Queue paling efisien diimplementasikan menggunakan collections.deque karena operasi di kedua ujung memiliki waktu O(1).
