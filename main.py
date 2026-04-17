from collections import deque
from datetime import datetime

class SistemParkirQueue:
    def __init__(self, kapasitas=20):
        self.queue = deque()          # Menggunakan Queue (deque)
        self.kapasitas = kapasitas
        self.riwayat = []             # Riwayat kendaraan yang sudah keluar

    def is_full(self):
        return len(self.queue) >= self.kapasitas

    def is_empty(self):
        return len(self.queue) == 0

    def parkir_masuk(self, nomor_plat, jenis_kendaraan):
        if self.is_full():
            print(f"❌ Parkiran penuh! Kapasitas maksimal: {self.kapasitas} kendaraan.")
            return False

        # Cek duplikat nomor plat
        for kendaraan in self.queue:
            if kendaraan['plat'].upper() == nomor_plat.upper():
                print(f"❌ Kendaraan dengan plat {nomor_plat} sudah berada di parkiran!")
                return False

        kendaraan = {
            'plat': nomor_plat.upper(),
            'jenis': jenis_kendaraan.lower(),
            'waktu_masuk': datetime.now()
        }

        self.queue.append(kendaraan)

        print(f"✅ Kendaraan {jenis_kendaraan} dengan plat {nomor_plat} berhasil masuk.")
        print(f"   Waktu masuk : {kendaraan['waktu_masuk'].strftime('%H:%M:%S')}")
        print(f"   Slot terisi  : {len(self.queue)}/{self.kapasitas}")
        return True 
