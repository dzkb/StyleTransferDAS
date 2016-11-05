import tkinter as tk
from StyleChooser import StyleChooser
from CameraImageProvider import CameraImageProvider

class Application(tk.Frame):
    def __init__(self, styles):
        self.root = tk.Tk()
        self.root.configure(bg="white", padx="10px", pady="10px")
        super().__init__(master = self.root,  bg="white")
        self.cameraImageProvider = CameraImageProvider()

        self.createTextSection("Welcome to magical style transfer from MedicalML")
        self.createStyleChooser(styles)
        self.createTextSection("+")
        self.createCameraLookup()
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
    @staticmethod
    def updateCameraLookup(app):
        app.imageLabel['image'] = app.cameraImageProvider.getImagePreview()
        app.root.after(50, Application.updateCameraLookup, app)
