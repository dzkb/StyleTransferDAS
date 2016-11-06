import tkinter as tk
from helpers import resizeImage
from PIL import Image
from AsyncTransformation import AsyncTransformation

class TransformationWindow(tk.Frame):
    imageSize = (600, 600)
    def __init__(self, transformer, imageRaw, modelPath):
        self.root = tk.Toplevel()
        self.root.configure(bg="white", padx="10px", pady="10px")
        super().__init__(master = self.root,  bg="white")

        self.imagesFrame = tk.Frame(self)
        self.addImageBefore(imageRaw)
        self.addEmptyImageAfter()

        self.imagesFrame.pack()
        self.pack()

        self.async = AsyncTransformation(transformer,
                                         imageRaw,
                                         modelPath,
                                         TransformationWindow.showTransformedImage,
                                         self)
        self.async.start()

    def addImageBefore(self, imageRaw):
        self.imageBefore = Image.fromarray(imageRaw)
        self.photoBefore = resizeImage(self.imageBefore, TransformationWindow.imageSize)
        self.imageLabel = tk.Label(self.imagesFrame, image=self.photoBefore)
        self.imageLabel.pack(side=tk.LEFT)
    def addEmptyImageAfter(self):
        self.imageAfter = TransformationWindow.emptyImage()
        self.photoAfter = resizeImage(self.imageAfter, self.imageBefore.size)
        self.imageLabel = tk.Label(self.imagesFrame, image=self.photoAfter)
        self.imageLabel.pack(side=tk.LEFT)

    @staticmethod
    def emptyImage():
        return Image.new(mode="RGB", size=TransformationWindow.imageSize)

    def showTransformedImage(self, rawTransformed):
        self.imageAfter = Image.fromarray(rawTransformed)
        self.photoAfter = resizeImage(self.imageAfter, self.imageBefore.size)
        self.imageLabel['image'] = self.photoAfter