import tkinter as tk
from StyleChooser import StyleChooser
from CameraImageProvider import CameraImageProvider
from ImageTransformer import ImageTransformer
from TransformationWindow import TransformationWindow

class Application(tk.Frame):
    buttonColor="#B3FF50"
    buttonText = "Make me artwork! \U000026C4"
    def __init__(self, styles):
        self.root = tk.Tk()
        self.root.configure(bg="white", padx="10px", pady="10px")
        super().__init__(master = self.root,  bg="white")
        self.cameraImageProvider = CameraImageProvider()
        self.imageTransformer = ImageTransformer()

        self.createTextSection("Welcome to magical style transfer from MedicalML")
        self.createStyleChooser(styles)
        self.createTextSection("+")
        self.createCameraLookup()
        self.createButton()
        self.pack()
    def createStyleChooser(self, styles):
        self.stylesFrame = StyleChooser(self, styles)

    def createTextSection(self, text, side=tk.TOP):
        self.nameLabel = tk.Label(master=self, text=text, font=("Helvetica", 25), bg="white")
        self.nameLabel.pack(side=side)

    def createCameraLookup(self):
        self.imageLabel = tk.Label(self)
        self.imageLabel.pack()
        Application.updateCameraLookup(self)

    def createButton(self):
        self.button = tk.Button(self,
                                text=Application.buttonText,
                                font=("Helvetica", 25),
                                bg=self.buttonColor)
        self.button.bind("<Button-1>", Application.displayImageTransformation)
        self.button.pack(expand=1)
    def getSelectedModelPath(self):
        return self.stylesFrame.getActiveStyle().modelpath

    @staticmethod
    def updateCameraLookup(app):
        app.imageLabel['image'] = app.cameraImageProvider.getImagePreview()
        app.root.after(50, Application.updateCameraLookup, app)

    @staticmethod
    def displayImageTransformation(event):
        appInstance = event.widget.master
        window = TransformationWindow(appInstance.imageTransformer,
                                      appInstance.cameraImageProvider.getImageRaw(),
                                      appInstance.getSelectedModelPath())

