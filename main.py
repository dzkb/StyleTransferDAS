from Style import Style
from Application import Application

transferedArtStyles = [
    Style("Starry night, Vincent van Gogh","images/starry-night.jpg"),
    Style("Scream, Edvard Munch","images/scream.jpg"),
    Style("Violin and candlestick,\nGeorges Braque", "images/violion-and-candlestick.jpg"),
    Style("Landscape at la ciotat,\nGeorges Braque", "images/landscape-at-la-ciotat.jpg"),
    Style("Dream, Salvadore Dali", "images/dream.jpg")
]
app = Application(styles=transferedArtStyles)
app.mainloop()