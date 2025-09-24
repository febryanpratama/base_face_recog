import pickle, os, time, cv2, face_recognition

ENCODINGS_PATH = "encodings.pkl"
DURATIONS_PATH = "durations.pkl"

# load encodings
with open(ENCODINGS_PATH, "rb") as f:
    known_faces = pickle.load(f)

# load durations
if os.path.exists(DURATIONS_PATH):
    with open(DURATIONS_PATH, "rb") as f:
        durations = pickle.load(f)
else:
    durations = {}

entry_times = {}

video = cv2.VideoCapture(0)
print("Membuka kamera... Tekan 'q' untuk keluar.")

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for face_encoding, face_location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(list(known_faces.values()), face_encoding)
        name = "Unknown"

        if True in matches:
            match_index = matches.index(True)
            name = list(known_faces.keys())[match_index]

            # kalau orang baru masuk
            if name not in entry_times:
                entry_times[name] = time.time()

            # hitung durasi
            durations[name] = durations.get(name, 0) + (time.time() - entry_times[name])
            entry_times[name] = time.time()

            top, right, bottom, left = face_location
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, f"{name} {int(durations[name])}s", (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

    cv2.imshow("Recognize Faces", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# simpan durations
with open(DURATIONS_PATH, "wb") as f:
    pickle.dump(durations, f)

video.release()
cv2.destroyAllWindows()