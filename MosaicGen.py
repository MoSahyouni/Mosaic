import math
import random
import numpy as np
from PIL import Image


class MosaicGenerator:
    def __init__(self, input, output, tiles, x, y):
        self.input = input
        self.output = output
        self.tiles = tiles
        self.x = x
        self.y = y


    

    @staticmethod
    def matchingTiles(img, tiles):
        print('finding average colors...')
        avgColors = []
        for img2 in tiles:
            colors = np.asarray(img2)
            imgColors = np.average(colors, axis=0)
            avgColor = np.average(imgColors, axis=0)
            avgColors.append(avgColor)

        print('finding best matches...')
        w = img.size[0]
        h = img.size[1]
        Matches = np.zeros((w, h), dtype=np.uint32)
        for i in range(w):
            for j in range(h):
                pxl = img.getpixel((i, j))
                similarity=[]

                for n in range(len(avgColors)):
                    similarity.append(MosaicGenerator.colorsSimilar(pxl, avgColors[n]))

                bestmatch1 = 0
                bestmatch2 = 1
                bestmatch3 = 2
                bestmatch4 = 3
                for n in range(len(similarity)):
                    if similarity[n]<=similarity[bestmatch1]:
                        bestmatch4 = bestmatch3
                        bestmatch3 = bestmatch2
                        bestmatch2 = bestmatch1
                        bestmatch1 = n
                    elif similarity[n]<=similarity[bestmatch2]:
                        bestmatch4 = bestmatch3
                        bestmatch3 = bestmatch2
                        bestmatch2 = n
                    elif similarity[n]<=similarity[bestmatch3]:
                        bestmatch4 = bestmatch3
                        bestmatch3 = n
                    elif similarity[n] <= similarity[bestmatch4]:
                        bestmatch4 = n

                bestmatch = []
                bestmatch.append(bestmatch1)
                bestmatch.append(bestmatch2)
                bestmatch.append(bestmatch3)
                bestmatch.append(bestmatch4)
                rnd = random.randint(0, 3)
                Matches[i][j] = bestmatch[rnd]
        return Matches

    @staticmethod
    def colorsSimilar(c1,c2):
        x1 = c1[0]
        y1 = c1[1]
        z1 = c1[2]
        x2 = c2[0]
        y2 = c2[1]
        z2 = c2[2]
        v = math.sqrt(math.pow((x1 - x2),2) + math.pow((y1 - y2),2) +math.pow((z1 - z2),2))
        return v

    @staticmethod
    def resize_input(img, x, y):
        print('resizing input image...')
        toResizeImg = Image.open(img)
        inputWidth = toResizeImg.size[0]
        inputHeight = toResizeImg.size[1]
        xx = 0
        yy = 0
        imgx = 0
        imgy = 0
        while (xx + x) <= inputWidth:
            xx += x
            imgx+=1
        while (yy + y) <= inputHeight:
            yy += y
            imgy+=1
        newImg = toResizeImg.resize((imgx, imgy))
        return newImg

    @staticmethod
    def replace_pixels(w1, h1, img, w2, h2, tiles, nearst_tiles):
        print('replacing pixels with tiles...')
        for i in range(w1):
            for j in range(h1):
                x = i * w2
                y = j * h2
                index = nearst_tiles[i][j]
                tile = tiles[index]
                img.paste(tile, (x, y))
        return img

    @staticmethod
    def save_result(img, name):
        img.save(name)
        print('mosaic image saved to '+ name)
        print('Displaying result image...')
        img.show(img)
