
from neuralstyle.generate import generate
from CameraImageProvider import CameraImageProvider


cip = CameraImageProvider()
raw = cip.getImageRaw()

img = generate("neuralstyle/models/composition.model", raw, _median_filter=0)