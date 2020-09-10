from picamera import PiCamera
from time import sleep

class Camera(object):
    camera = None
    def __init__(self):
        Camera.camera = PiCamera()
        self.default_location = '/home/pi/'

    def take_picture(self, resolution=(640, 480), location='/home/pi/picture.jpg'):
        camera.resolution = resolution
        camera.capture(location)

camera = PiCamera()
camera.resolution = (640, 480)

camera.capture('/home/pi/projects/capture.jpg')