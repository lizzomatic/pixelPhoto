from PIL import Image
import os

def getName(imagePath):
    imagePath = os.path.basename(imagePath)  # returns name of the file
    iList = imagePath.split('.')
    imageName = iList[0]
    return imageName

def makeGif(imagePath, antialias='lanczos', imgQuality=10):
    img = Image.open(imagePath)
    width, height = img.size
    qWidth = round(width/imgQuality)
    qHeight = round(height/imgQuality)
    if antialias == 'lanczos':
        small_img = img.resize((qWidth, qHeight), Image.Resampling.LANCZOS)
    elif antialias == 'bilinear':
        small_img = img.resize((qWidth, qHeight), Image.Resampling.BILINEAR)

    # resize
    oSize = (width, height)  # output size
    imgNew = small_img.resize(oSize, Image.Resampling.NEAREST)

    # save image
    imageName = getName(imagePath)
    imgNew.save(imageName + '_pixel.png')
