from PIL import ImageTk, Image

def bindWithChildren(widget, event, callback, add=''):
    "Binds an event to a widget and all its descendants."

    widget.bind(event, callback, add)

    for child in widget.children.values():
        bindWithChildren(child, event, callback, add)

def resizeImage(image, size):
    image.thumbnail(size, Image.ANTIALIAS)
    return ImageTk.PhotoImage(image)