from PIL import Image
import covertModel

img = Image.open("download.png")
blackAndWhite = img.convert("L")
blackAndWhite.save('vathanaB.png')
blackAndWhite.show()