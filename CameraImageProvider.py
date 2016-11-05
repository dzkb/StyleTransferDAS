from PIL import Image, ImageTk
import cv2

class CameraImageProvider:
    cameraID = 0 # 0 for integrated cam, 1 for first external can ....
    def __init__(self):
        self.cap = cv2.VideoCapture(CameraImageProvider.cameraID)
    def getImagePreview(self):
        image = Image.fromarray(self.getImageRaw())
        image.thumbnail((200,200), Image.ANTIALIAS)
        self.lastFrame = ImageTk.PhotoImage(image)
        return self.lastFrame
    def getImageRaw(self):
        ret, frame = self.cap.read()
        return frame
