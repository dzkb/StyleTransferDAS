import tkinter as tk
from PIL import Image, ImageTk
from helpers import bindWithChildren, resizeImage

class StyleFrame(tk.Frame):
    imageSize=(200,200)
    colorActive="#B3FF50"
    colorInactive="white"
    def __init__(self, parentFrame, style):
        super().__init__(master = parentFrame, background="white", padx="10px", pady="10px")
        self.parent=parentFrame
        self.createImageLabel(self, style.filepath)
        self.createTextLabel(self, style.name)
        self.setLabelsBackground(StyleFrame.colorInactive)
        self.pack(fill='y', side=tk.LEFT)

    def createImageLabel(self, parentFrame, path):
        self.photo = resizeImage(Image.open(path), StyleFrame.imageSize)
        self.imageLabel = tk.Label(parentFrame, image=self.photo, padx=500)
        self.imageLabel.pack()
    def createTextLabel(self, parentFrame, stylename):
        self.nameLabel = tk.Label(master=parentFrame, text=stylename)
        self.nameLabel.pack(fill=tk.X)
    def hasInFrame(self, widget):
        return widget in [self, self.imageLabel, self.nameLabel]
    def setLabelsBackground(self, color):
        self.imageLabel["bg"] = color
        self.nameLabel["bg"] = color
    def setActive(self):
        self.setLabelsBackground(StyleFrame.colorActive)
    def setUnactive(self):
        self.setLabelsBackground(StyleFrame.colorInactive)

# use getActiveStyle() to get currently selected Style object
class StyleChooser(tk.Frame):
    instance = 0
    def __init__(self, parentFrame, styles):
        super().__init__(master = parentFrame)
        self.initializeSingleton()
        self.createFramesForStyles(styles)
        self.setActiveStyle(list(self.frameToStyleMap.keys())[0])
        self.registerClickHandler()
        self.pack()

    def createFramesForStyles(self, styles):
        self.frameToStyleMap = dict()
        for style in styles:
            self.frameToStyleMap[StyleFrame(self, style)] = style
    def getActiveStyle(self):
        return self.activeStyle
    def registerClickHandler(self):
        bindWithChildren(self, "<Button-1>", StyleChooser.handleClick)
    def initializeSingleton(self):
        if StyleChooser.instance != 0: assert False
        StyleChooser.instance = self
    def setActiveStyle(self, styleFrame):
        self.deactivateAllStyleframes()
        styleFrame.setActive()
        self.activeStyle = self.frameToStyleMap[styleFrame]
    def deactivateAllStyleframes(self):
        for styleFrame in self.frameToStyleMap.keys():
            styleFrame.setUnactive()

    @staticmethod
    def handleClick(event):
        clickedWidget = event.widget
        styleChooserSingleton = StyleChooser.instance
        for styleFrame in styleChooserSingleton.frameToStyleMap.keys():
            if styleFrame.hasInFrame(clickedWidget):
                styleChooserSingleton.setActiveStyle(styleFrame)
                break