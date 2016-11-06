from PIL import Image, ImageTk
import cv2
from helpers import resizeImage

class CameraImageProvider:
    cameraID = 0 # 0 for integrated cam, 1 for first external can ....
    previewSize = (200,200)
    def __init__(self):
        self.cap = cv2.VideoCapture(CameraImageProvider.cameraID)
    def getImagePreview(self):
        self.lastFrame = resizeImage(Image.fromarray(self.getImageRaw()), CameraImageProvider.previewSize)
        return self.lastFrame
    def getImageRaw(self):
        _, frame = self.cap.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        return frame
