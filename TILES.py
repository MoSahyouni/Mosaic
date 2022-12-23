import glob
from PIL import Image

class Tiles:
    def import_tiles(path):
        print('getting tiles paths...')
        pathsArr = []
        for imgName in glob.iglob(path):
            pathsArr.append(imgName)

        print('importing tiles...')
        tilesArr=[]
        for path in pathsArr:
            tile = Image.open(path)
            tilesArr.append(tile)
        return tilesArr

    def getresizedTiles(tiles, size):
        resized = []
        tilesArr = Tiles.import_tiles(tiles)
        print('resizing Tiles...')
        for tile in tilesArr:
            tile = tile.resize(size)
            resized.append(tile)
        return resized
