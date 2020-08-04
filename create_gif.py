import argparse
from os import listdir
from os.path import isfile, join

from PIL import Image


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--folder", type=str, default="data/samples", help="path to dataset")
    opt = parser.parse_args()

    files = [f for f in listdir(opt.folder) if isfile(join(opt.folder, f))]
    files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
    
    images = []
    for f in files:
        images.append(Image.open(f"{opt.folder}/{f}"))

    images[0].save('teste.gif', save_all=True, append_images=images[1:], optimize=False, duration=40, loop=0)