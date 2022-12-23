import argparse
import os
import sys
from PIL import Image
from TILES import Tiles
from MosaicGen import MosaicGenerator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='input_img')
    parser.add_argument('-o', dest='output_img',default='mosaic.jpg')
    parser.add_argument('-t', dest='tiles_dir',default='tiles')
    parser.add_argument('-x', dest='x', default=10)
    parser.add_argument('-y', dest='y', default=10)
    args = parser.parse_args()

    input2 = str(args.input_img)
    output = str(args.output_img)
    tiles = str(args.tiles_dir)
    x = int(str(args.x))
    y = int(str(args.y))

    if len(sys.argv) > 1:
        if not os.path.isfile(input2):
            print('! ERROR input Image not found'.format(input2))
        elif not os.path.isdir(tiles):
            print('! ERROR input tiles not found'.format(tiles))
        else:
            print('Starting...')
            Mosaic = MosaicGenerator(input2, output, tiles, x, y)
            resizedTiles = Tiles.getresizedTiles(Mosaic.tiles + '/*', (x, y))
            inputImgResized = Mosaic.resize_input(Mosaic.input, x, y)
            pixelsMatches = Mosaic.matchingTiles(inputImgResized, resizedTiles)
            OutputImg = Image.new('RGB', Image.open(Mosaic.input).size)
            newImage = Mosaic.replace_pixels(inputImgResized.size[0],
                                             inputImgResized.size[1], OutputImg,
                                             x, y, resizedTiles, pixelsMatches)
            Mosaic.save_result(newImage, Mosaic.output)
            print('finished.')

if __name__ == '__main__':

    main()