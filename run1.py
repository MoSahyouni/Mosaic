import os
from PIL import Image
from MosaicGen import MosaicGenerator
from TILES import Tiles

def main():
    input_img = input('input image name:')
    output_img = input('output image name:')
    tiles_dir = input('type tiles directory name:')
    xinput = input('insert width of tiles:')
    yinput  = input('insert height of tiles:')

    '''defualt inputs'''
    output='mosaic.jpg'
    tiles ='tiles'
    x=10
    y=10

    '''set giving input'''
    if str(input_img) != '':
        input2 = str(input_img)
    if str(output_img) != '':
        output = str(output_img)
    if str(tiles_dir) != '':
        tiles = str(tiles_dir)
    if str(xinput) != '':
        x = int(str(xinput))
    if str(yinput) != '':
        y = int(str(yinput))

    if not os.path.isfile(input2):
        print('! ERROR input Image not found'.format(input2))
    elif not os.path.isdir(tiles):
        print('! ERROR tiles Dir not found'.format(tiles))
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