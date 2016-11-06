from threading import Thread

class AsyncTransformation(Thread):
    def __init__(self, transformer, imageRaw, modelPath, notifyFunction, notifyObject):
        Thread.__init__(self)
        self.transformer = transformer
        self.imageRaw = imageRaw
        self.modelPath = modelPath
        self.notifyFunction = notifyFunction
        self.notifyObject = notifyObject

    def run(self):
        transformedImage = self.transformer.transform(self.imageRaw, self.modelPath)
        self.notifyFunction(self.notifyObject, transformedImage)