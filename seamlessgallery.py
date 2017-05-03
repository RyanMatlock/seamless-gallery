#!/usr/bin/env python3
"""
igpanocrop.py

crops wide images into a series of consecutive square images using ImageMagick 
(I've used convert on the command line enough that I'd rather just interface 
with that rather than looking into pillow, which seems to be rather old anyway)
"""

import subprocess
import shlex
import os
import sys
import logging
import argparse
import datetime


def get_img_dimensions(img):
    # http://stackoverflow.com/questions/6657690/python-getoutput-equivalent-in-subprocess
    # specifically http://stackoverflow.com/a/6657718/2677392
    get_dim_process = subprocess.Popen(shlex.split(r"identify -format "
                                            '"%[fx:w],%[fx:h]" '
                                            "{}".format(img)),
                                    stdout=subprocess.PIPE)
    raw_dim, err = get_dim_process.communicate()
    logging.debug("type(raw_dim): {}; raw_dim: {}"
                  "".format(type(raw_dim), raw_dim))
    # raw_dim is a bytes type object
    try:
        return tuple([int(dim) for dim in raw_dim.decode("utf-8").split(",")])
    except ValueError as e:
        print("{} doesn't seem to work nicely with ImageMagick identify. "
              "Maybe it isn't a valid image file?".format(img))
        raise e

def crop_images(img, dest):
    width, height = get_img_dimensions(img)
    aspect_ratio = int(width / height)

    ext = os.path.splitext(img)[1]

    for i in range(aspect_ratio):
        left_offset = i * height
        output_path = os.path.join(dest, str(i+1) + ext)
        logging.debug("output_path: {}".format(output_path))
        subprocess.Popen(shlex.split("convert {} -crop {}x{}+{}+0 {}"
                                     "".format(img,
                                               height,
                                               height,
                                               left_offset,
                                               output_path))).wait()
    

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_image",
                    help="path to wide image, which will be split up into "
                         "a series of adjacent square images")
    ap.add_argument("-d",
                    "--dir",
                    help="output directory to which square images will be "
                         "saved; if none is specified, a timestamped "
                         "igpanocrop folder will be created in the current "
                         "working directory")

    args = ap.parse_args()

    logging.debug(get_img_dimensions(args.input_image))

    if not args.dir or not os.path.isdir(args.dir):
        output_dir = (os.path.join(os.getcwd(),
                      "igpanocrop_" +
                      datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")))
        os.mkdir(output_dir)
    else:
        output_dir = args.dir
    logging.debug("output_dir: {}".format(output_dir))

    crop_images(args.input_image, output_dir)

    return 0


if __name__ == "__main__":
    sys.exit(main())
