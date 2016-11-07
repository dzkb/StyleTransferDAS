from PIL import Image
from chainer import serializers, cuda, Variable
from net import *
import numpy as np
from time import sleep

from neuralstyle.generate import generate

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
        generated = generate(modelPath, image)
        print("ok")
        return generated


    def loadModelFromPath(self, modelPath):
        print("start loading")
        if self.modelPath != modelPath:
            serializers.load_npz(modelPath, self.model)
            if RUN_ON_GPU:
                cuda.get_device(0).use() #assuming only one core
                self.model.to_gpu()
        print("loaded")