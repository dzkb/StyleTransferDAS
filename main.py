from Style import Style
from Application import Application

transferedArtStyles = [
    Style("Starry night, Vincent van Gogh",             "images/starry-night.jpg", "neuralstyle/models/composition.model"),
    Style("Scream, Edvard Munch",                       "images/scream.jpg", "models/cubist.model"),
    Style("Violin and candlestick,\nGeorges Braque",    "images/violion-and-candlestick.jpg", "models/cubist.model"),
    Style("Landscape at la ciotat,\nGeorges Braque",    "images/landscape-at-la-ciotat.jpg", "models/cubist.model"),
    Style("Dream, Salvadore Dali",                      "images/dream.jpg", "models/cubist.model")
]
app = Application(styles=transferedArtStyles)
app.mainloop()