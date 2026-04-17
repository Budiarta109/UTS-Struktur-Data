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
def parkir_keluar(self):
        if self.is_empty():
            print("❌ Parkiran kosong! Tidak ada kendaraan yang bisa keluar.")
            return False

        # Keluarkan kendaraan pertama (FIFO)
        kendaraan_keluar = self.queue.popleft()
        waktu_keluar = datetime.now()

        # Hitung durasi
        durasi = waktu_keluar - kendaraan_keluar['waktu_masuk']
        jam = int(durasi.total_seconds() // 3600)
        menit = int((durasi.total_seconds() % 3600) // 60)
Hitung biaya
        if kendaraan_keluar['jenis'] == "mobil":
            biaya = (jam * 5000) + (menit * 100 if menit > 0 else 0)
        else:  # motor
            biaya = (jam * 3000) + (menit * 50 if menit > 0 else 0)

        print(f"\n🚗 KENDARAAN KELUAR (FIFO)")
        print(f"   Nomor Plat     : {kendaraan_keluar['plat']}")
        print(f"   Jenis          : {kendaraan_keluar['jenis'].capitalize()}")
        print(f"   Waktu Masuk    : {kendaraan_keluar['waktu_masuk'].strftime('%H:%M:%S')}")
        print(f"   Waktu Keluar   : {waktu_keluar.strftime('%H:%M:%S')}")
        print(f"   Durasi         : {jam} jam {menit} menit")
        print(f"   Biaya Parkir   : Rp {int(biaya):,}")

        # Simpan ke riwayat
        self.riwayat.append({
            'plat': kendaraan_keluar['plat'],
            'jenis': kendaraan_keluar['jenis'],
            'masuk': kendaraan_keluar['waktu_masuk'],
            'keluar': waktu_keluar,
            'biaya': biaya,
            'durasi': f"{jam} jam {menit} menit"
        })

        print(f"✅ Kendaraan berhasil keluar. Slot tersisa: {len(self.queue)}/{self.kapasitas}")
        return True

    def tampilkan_parkiran(self):
        if self.is_empty():
            print("\n🅿️  Parkiran saat ini kosong.")
            return

        print(f"\n🅿️  STATUS PARKIRAN - QUEUE (FIFO)")
        print(f"   Total terisi : {len(self.queue)}/{self.kapasitas}")
        print("=" * 65)
        print(f"{'No':<3} {'Plat Nomor':<15} {'Jenis':<10} {'Waktu Masuk':<20}")
        print("=" * 65)
for i, kendaraan in enumerate(self.queue, 1):
            print(f"{i:<3} {kendaraan['plat']:<15} {kendaraan['jenis'].capitalize():<10} "
                  f"{kendaraan['waktu_masuk'].strftime('%H:%M:%S')}")

    def tampilkan_riwayat(self):
        if not self.riwayat:
            print("\nBelum ada riwayat parkir.")
            return

        print("\n📋 RIWAYAT PARKIR (Kendaraan yang sudah keluar)")
        print("=" * 80)
        for i, r in enumerate(self.riwayat, 1):
            print(f"{i:2}. {r['plat']:<12} | {r['jenis'].capitalize():<8} | "
                  f"{r['durasi']:<15} | Rp {int(r['biaya']):,}")
