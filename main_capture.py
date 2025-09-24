import cv2
import face_recognition
import pickle
import os

ENCODINGS_PATH = "encodings.pkl"

# Load database wajah lama (kalau ada)
if os.path.exists(ENCODINGS_PATH):
    with open(ENCODINGS_PATH, "rb") as f:
        known_faces = pickle.load(f)
else:
    known_faces = {}

cap = cv2.VideoCapture(0)
print("Membuka kamera... Tekan 'c' untuk capture wajah, 'q' untuk keluar.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    cv2.imshow("Capture Wajah", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('c'):
        name = input("Masukkan nama untuk wajah ini: ")
        face_locations = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        if encodings:
            known_faces[name] = encodings[0]
            with open(ENCODINGS_PATH, "wb") as f:
                pickle.dump(known_faces, f)
            print(f"✅ Wajah {name} berhasil dicapture & disimpan!")
        else:
            print("❌ Tidak ada wajah terdeteksi.")
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()