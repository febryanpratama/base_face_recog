# Face Recognition Cafe Demo

Proyek ini adalah contoh implementasi **Face Recognition** menggunakan Python, `face_recognition`, dan OpenCV.  
Fitur utama:
- Capture wajah dan simpan ke file `encodings.pkl`
- Recognize wajah yang sudah tercapture
- Hitung lama waktu (durasi) seseorang berada di depan kamera (menit / detik)
- Simpan data durasi ke `durations.pkl`

Cocok untuk use case seperti **presensi karyawan** atau **monitoring customer di cafe**.

---

## 🚀 Setup Environment

1. Clone / salin repository ini  
   ```bash
   git clone <repo-url>
   cd face_recognition
   ```

2. Buat Virtual Environtment

    ```bash
    python3 -m venv facerecog_api
    source facerecog_api/bin/activate
    ```
    
Running API
Mau saya bikinkan juga contoh **requirements.txt** isi pastinya biar sekali jalan `pip install -r requirements.txt` langsung berhasil?