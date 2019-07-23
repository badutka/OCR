import json
import numpy as np
import string
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import os
import io


def main():
    size = 128, 128
    i = 0
    l = []
    images = []
    d = {}

    with open("data_set.json", "w") as file:
        file.write(json.dumps({}))

    for subdir, dirs, files in os.walk("Img"):

        if i == 0:
            i += 1
        else:
            i += 1
            if i == 52:
                break

            for im in files:
                with Image.open(str(subdir) + "/" + str(im)) as img:
                    img = img.resize((40, 40), Image.ANTIALIAS)
                    iar = convert(img)
                    # iar = np.array(img)
                    d[str(im)] = {}

                    json_encoder(str(im), iar, d)

                    name = str(im).split(".")

                    with open("data_sets/" + name[0] + ".json", "w") as file:
                        file.write(json.dumps(d[str(im)], indent=4, sort_keys=False))

                    d = {}

    '''for i in images:
    for j in range(len(images[0])):
        for x in range(len(images[0][j])):
            for y in range(len(images[0][j][x])):
                if images[0][j][x][y]<135:
                    images[0][j][x][y]=0
                else:
                    images[0][j][x][y]=255'''


def convert(img):
    iar = np.array(img)

    for j in range(len(iar)):

        for x in range(len(iar[j])):

            for y in range(len(iar[j][x])):
                if iar[j][x][y] < 127:
                    iar[j][x][y] = 255 - iar[j][x][y]
                else:
                    iar[j][x][y] = 255 - iar[j][x][y]

    return iar


def show_image_table(iar):
    x = 1
    y = 1
    for i in iar:
        for j in i:
            print(str(x) + " " + str(y) + " " + str(j))
            x += 1
        y += 1
        x = 1


def parse_data(iar):
    d = {}
    x = 1
    y = 1
    l = [0, 0, 0]
    for i in iar:
        for j in i:
            # print(str(x) + " " + str(y) + " " + str(j))
            pixel = " ".join([str(x), str(y)])

            d[pixel] = int(j[0])
            x += 1
        y += 1
        x = 1

    return d


def json_encoder(name, iar, d):
    # with open("data_set.json", "w") as file:

    data = parse_data(iar)
    d[name] = {}
    for i, j in data.items():
        d[name][i] = j

    '''img = Image.fromarray(images[0], 'RGB')
    img.save('my.png')
    img.show()'''

    '''x = 1
    y = 1
    for i in images[0]:
        for j in i:
            print(str(x) + " " + str(y) + " " + str(j))
            x += 1
        y += 1
        x = 1'''

    # img = Image.fromarray(data, 'RGB')
    '''y = 1
    for i in images[0]:
        for j in i:
            print(str(x) + " " + str(y) + " " + str(j))
            x += 1
        y += 1
        x = 1'''

    '''x=1
    y=1
    for i in iar:
        for j in i:
            print(str(x) + " " + str(y) + " " + str(j))
            x+=1
        y+=1
        x=1'''

    # with open('Train.csv', 'w') as F:
    #     F.write('\n'.join(l))


if __name__ == "__main__":
    main()
