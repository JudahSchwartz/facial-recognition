# import face_recognition
import sys
import cv2


cam = cv2.VideoCapture(0)


def find_angle_to_adjust(pos, total, name):
    x = (pos / total) * 100
    print(f"{name} is {x} percent of camera, {pos=} {total=}")


while True:
    ret, frame = cam.read()
    dimensions = frame.shape


    print(dimensions)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if ret:
        face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face_profile_cascade = cv2.CascadeClassifier('profile.xml')

        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        faces_prof = face_profile_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    else:
        faces = []
        faces_prof = []

    for arr, color in [(faces, True), (faces_prof, False)]:
        for (x, y, w, h) in arr:
            x_mid = x + w // 2
            y_mid = y + h // 2

            angle_x = find_angle_to_adjust(x_mid, dimensions[1], 'x')
            angle_y = find_angle_to_adjust(y_mid, dimensions[0], 'y')

            cv2.rectangle(frame, (x_mid, y_mid), (x_mid + 1, y_mid + 1), (0, 0 if color else 255, 255 if color else 0), 20)
    cv2.imshow('Image', frame)
    # if input("Exit") == 'y':
    #     sys.exit(0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    sys.exit(0)