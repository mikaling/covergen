# CoverGen - Playlist Cover Generator

import os
from PIL import Image

images =[
    './input/1.jpg',
    './input/2.jpg',
    './input/3.jpg',
    './input/4.jpg',
]

positions = [
    (0, 0,),
    (500, 0),
    (500, 500),
    (0, 500),
    (250, 500),
    (250, 750),
    (0, 750),
    (125, 750),
    (125, 875),
    (0, 875)
]

count = 0

result = Image.new("RGB", (1000, 1000))

for i in range(3):
    if i != 2:
        for index in range(len(images) - 1):
            path = os.path.expanduser(images[index])
            new_image = Image.open(path)
            new_size = 2 ** -(i + 1) * 1000
            new_image.thumbnail((new_size, new_size), Image.ANTIALIAS)
            x = positions[count][0]
            y = positions[count][1]
            width, height = new_image.size
            print(index)
            print('pos {0},{1} size {2},{3}'.format(x, y, width, height))
            result.paste(new_image, (x, y, x + width, y + height))
            count += 1
    elif i == 2:
        for index2 in range(len(images)):
            path = os.path.expanduser(images[index2])
            new_image = Image.open(path)
            new_size = 2 ** -(i + 1) * 1000
            new_image.thumbnail((new_size, new_size), Image.ANTIALIAS)
            x = positions[count][0]
            y = positions[count][1]
            width, height = new_image.size
            print(index2)
            print('pos {0},{1} size {2},{3}'.format(x, y, width, height))
            result.paste(new_image, (x, y, x + width, y + height))
            count += 1

result.save(os.path.expanduser('./output/cover.jpg'))