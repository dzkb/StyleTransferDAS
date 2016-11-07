from time import sleep

from chainer import serializers, cuda
from neuralstyle.net import FastStyleNet
from neuralstyle.generate import generate
import config

## TODO:
#  cant parse more than one at once because
#  instance is shared between threads
#  causing common model and ???
##

class ImageTransformer:
    def __init__(self):
        self.model = FastStyleNet()
        self.modelPath = ""
        
    def transform(self, image, modelPath):
        self.loadModelFromPath(modelPath)
        return generate(self.model, image)


    def loadModelFromPath(self, modelPath):
        if self.modelPath != modelPath:
            self.modelPath = modelPath
            print "start loading model: ", modelPath
            serializers.load_npz(modelPath, self.model)
            if config.RUN_ON_GPU:
                cuda.get_device(config.GPU_UNIT).use() #assuming only one core
                self.model.to_gpu()