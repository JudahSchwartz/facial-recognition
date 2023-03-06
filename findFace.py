# import face_recognition
import cv2


cam = cv2.VideoCapture(0)
while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        print(f"{x=} {y=} {w=} {h=}")
        x_mid = x + w // 2
        y_mid = y + h // 2
        cv2.rectangle(frame, (x_mid, y_mid), (x_mid + 1, y_mid + 1), (0, 0, 255), 20)
    cv2.imshow('Image', frame)
    cv2.destroyAllWindows()