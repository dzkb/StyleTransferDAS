from chainer import serializers, cuda, Variable
from net import *
import numpy as np
from time import sleep

RUN_ON_GPU = False
class ImageTransformerMock():
    def transform(self, image, modelPath):
        sleep(3)
        return image
class ImageTransformer:
    def __init__(self):
        self.model = FastStyleNet()
        self.modelPath = ""
        
    def transform(self, image, modelPath):
        self.loadModelFromPath(modelPath)

        xp = np if not RUN_ON_GPU else cuda.cupy

        image = xp.asarray(image, dtype=xp.float32).transpose(2, 0, 1)
        image = image.reshape((1,) + image.shape)
        image -= 120

        x = Variable(image)
        y = self.model(x)

        result = cuda.to_cpu(y.data)
        result = result.transpose(0, 2, 3, 1)
        result = result.reshape((result.shape[1:]))
        result += 120
        result = np.uint8(result)
        return result


    def loadModelFromPath(self, modelPath):
        print("start loading")
        if self.modelPath != modelPath:
            serializers.load_npz(modelPath, self.model)
            if RUN_ON_GPU:
                cuda.get_device(0).use() #assuming only one core
                self.model.to_gpu()
        print("loaded")