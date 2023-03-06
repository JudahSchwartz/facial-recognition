import face_recognition
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

# make the list of all available cameras
camlist = pygame.camera.list_cameras()
print(camlist)
# if camera is detected or not
if camlist:
    # initializing the cam variable with default camera
    cam = pygame.camera.Camera(camlist[0], (640, 480))

    # opening the camera
    cam.start()

    # capturing the single image
    image = cam.get_image()

    # saving the image
    pygame.image.save(image, "filename.jpg")

image = face_recognition.load_image_file("filename.jpg")
face_locations = face_recognition.face_locations(image)