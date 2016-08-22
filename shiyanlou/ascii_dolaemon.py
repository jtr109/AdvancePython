from PIL import Image
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file')  # input file
parser.add_argument('-o', '--output')  # output file
parser.add_argument('--width', type=int, default=80)
parser.add_argument('--height', type=int, default=80)

args = parser.parse_args()

IMG = args.file
OUTPUT = args.output
WIDTH = args.width
HEIGHT = args.height

ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")


def get_char(r, b, g, alpha=256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * b + 0.0722 * g)

    unit = 256.0 / length
    return ascii_char[int(gray / unit)]


if __name__ == '__main__':

    im = Image.open(IMG)
    # im.thumbnail((WIDTH, HEIGHT), Image.NEAREST)
    # the 'im.thumbnail' will not change the proportion of width and height
    new_im = im.resize((WIDTH, HEIGHT), Image.NEAREST)

    l = []

    for i in range(HEIGHT):
        for j in range(WIDTH):
            l.append(get_char(*new_im.getpixel((j, i))))
        l.append('\n')

    txt = ''.join(l)

    print(txt)

    if OUTPUT:
        with open(OUTPUT, 'w') as f:
            f.write(txt)
    else:
        with open('output.txt', 'w') as f:
            f.write(txt)
