from PIL import Image, ImageTk
import cv2
from helpers import resizeImage

class CameraImageProvider:
    cameraID = 0 # 0 for integrated cam, 1 for first external can ....
    def __init__(self):
        self.cap = cv2.VideoCapture(CameraImageProvider.cameraID)
    def getImagePreview(self):
        self.lastFrame = resizeImage(Image.fromarray(self.getImageRaw()), (200,200))
        return self.lastFrame
    def getImageRaw(self):
        ret, frame = self.cap.read()
        return frame
