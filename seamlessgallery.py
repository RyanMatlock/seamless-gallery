#!/usr/bin/env python3
"""
seamlessgallery.py

crops wide images into a series of consecutive images using ImageMagick

(there are probably better ways of doing this, but I got this to work pretty 
quickly)

TODOs
- [ ] add flag to include "rest" of image
- [ ] check to see if IG lets you use aspect ratios other than 1:1 for seamless
  galleries; if it does, add a flag to specify the desired aspect ratio within
  the limits of what IG allows -- it looks like you can, so do this!!
  (dimensions limited to between 1.91:1 and 4:5, but you're presumably going
  between square and 4:5, so I'll just make the latter an option)
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


def crop_images(img, dest, output_aspect_ratio):
    width, height = get_img_dimensions(img)
    ext = os.path.splitext(img)[1]
    logging.debug("img stats:\n\t"
                  "width: {}\n\t"
                  "height: {}\n\t"
                  "ext (i.e. filetype): {}"
                  "".format(width, height, ext))

    # While output_ar_width/height *could* be floats, I'm going to keep them as
    # ints because I think weird rounding errors could happen otherwise, and
    # I'm only doing 1:1 and 4:5 right now. The right answer is probably to
    # store them as demical.Decimal values, but I can do that at a later date
    output_ar_width, output_ar_height = \
      tuple([int(x) for x in output_aspect_ratio.split(":")])
    logging.debug("output aspect ratio: {}:{}"
                  "".format(output_ar_width, output_ar_height))

    output_width = int((height / output_ar_height) * output_ar_width)
    logging.debug("output_width: {}".format(output_width))
    num_of_images = int(width / output_width)
    logging.debug("num_of_images: {}".format(num_of_images))

    for i in range(num_of_images):
        left_offset = i * output_width
        output_path = os.path.join(dest, str(i+1) + ext)
        logging.debug("output_path: {}".format(output_path))
        subprocess.Popen(shlex.split("convert {} -crop {}x{}+{}+0 {}"
                                     "".format(img,
                                               output_width,
                                               height,
                                               left_offset,
                                               output_path))).wait()

        
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_image",
                    help="path to wide image, which will be split up into "
                         "a series of adjacent images")
    ap.add_argument("-d",
                    "--dir",
                    help="output directory to which output images will be "
                         "saved; if none is specified, a timestamped "
                         "seamlessgallery folder will be created in the "
                         "current working directory")

    ap.add_argument("-p",
                    "--portrait",
                    action="store_true",
                    help="outputs a series of 4:5 aspect ratio images instead "
                         "of the default 1:1 aspect ratio (NOTE: as of "
                         "2017-05-05, Instagram doesn't seem to like "
                         "non-square galleries, so for now at least, it isn't "
                         "recommended that you use this feature")


    args = ap.parse_args()

    logging.debug(get_img_dimensions(args.input_image))

    if not args.dir or not os.path.isdir(args.dir):
        output_dir = (os.path.join(os.getcwd(),
                      "seamlessgallery_" +
                      datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S")))
        os.mkdir(output_dir)
    else:
        output_dir = args.dir
    logging.debug("output_dir: {}".format(output_dir))

    if args.portrait:
        ar = "4:5"
    else:
        ar = "1:1"

    crop_images(args.input_image, output_dir, ar)

    return 0


if __name__ == "__main__":
    sys.exit(main())
