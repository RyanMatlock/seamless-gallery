# Description
`seamlessgallery` makes it "easy" to take advantage of the fact that on phones,
Instagram galleries are displayed with no seam between images, so if you scroll
slowly between images, you get the illusion that you're looking at a chunk of a
panorama if the discrete images were all carefully cut from one master
image. (It's probaly easiest to try this out and then see what I mean.)

# A simple example
Once you have `seamlessgallery` installed, you should be able to run it like
so:

```
$ seamlessgallery /path/to/test.jpg
```

which will generate a timestamped folder
(e.g. `seamlessgallery-1969-12-31-115959`) containing a series of adjacent
square images with sequential whole number names (e.g. `1.jpg`, `2.jpg`, ...).

# Requirements
- [Python 3](https://www.python.org/)
- [ImageMagick](https://www.imagemagick.org/script/index.php)

(Windows users may need something like cygwin, and to be honest, I've only
tested this on Mac OS X.) While you can install binaries using the links above,
in my opinion, it's easiest to use a package manager
(e.g. [Homebrew](https://brew.sh/) for Mac OS X or `apt-get` on Debian-based
Linux distros like Ubuntu) to get everything working nicely.

To ensure everything's installed properly, enter the following commands:

```
$ which python3
$ which identify
$ which convert
```

which should all return a path to the program in question (e.g. on my system,
each program resides in `/usr/local/bin`, so `$ which python3` returns
`/usr/local/bin/python3`). If `which` doesn't return a value, something has
gone wrong.

# Installation
(When it comes to Windows, I'm basically clueless, so you're kind of on your
own.)

Personally, I like keeping this project directory in a folder where I keep my
scripts (for the purposes of the following instructions, I'll assume that
everything is in `~/misc-scripts/seamless-gallery`, but you may choose to place
the repo elsewhere, in which case you'll have to update the paths accordingly),
then I symlink it to somewhere on my `PATH` (to figure out which folders are on
your path, simply enter

```
$ echo $PATH
```

to see a list of directories on your `PATH`). Before symlinking it, it needs
the appropriate permissions (i.e. it needs to be executable). To do that, run

```
$ chmod +x ~/misc-scripts/seamless-gallery/seamlessgallery.py
```

Next create the symlink. For example, in this situation, I would run

```
$ ln -s ~/misc-scripts/seamless-gallery/seamlessgallery.py
/usr/local/bin/seamlessgallery
```

in order to be able to call `seamlessgallery` without having to go to the
trouble of pointing the shell to the script.

To ensure it's properly installed, you can try running our old friend

```
$ which seamlessgallery
```

(apparently this only returns a path if `seamlessgallery` is an
executable---good to know) or better still, try running

```
$ seamlessgallery -h
```

and if everything's working properly, the help menu should appear.


# Options
## `-d`, `--dir` directory flag
If you don't want the output images to be written to a timestamped folder in
the current working directory, the `-d` or `--dir` flag can be used to specify
a different directory in which to place the output images. If the directory
doesn't exist, it will be created. **WARNING**: if the directory already
exists, files that are already there will be overwritten if they have the same
name as the output files (e.g. `1.jpg`, `2.jpg`, ...). At this point in time, I
have no plans to make a more flexible naming scheme.

# Workflow
Given that Instagram requires that you use your phone to upload images and this
script is most easily run on a computer, you're sacrificing a bit of
convenience to get this result.

Once you have a panoramic/wide image on your computer, it's as simple as
running the script on the image in order to generate the series of square
images for Instagram. From there, I move the images back onto my phone using
Dropbox, but you're welcome to do it any way you'd like (Mac + iPhone users
have the option of Airdrop, I believe). After that, just open up Instagram and
make sure to choose the photos in the right order (you'll be able to preview
the order before publishing the gallery). That's it!

# Suggestions
If you've used this script and have a public Instagram account, it would be
great if you could tag the gallery with `#seamlessgallery` so I could see your
work!

If you want to have the most control over the results, I suggest cropping
within Lightroom (or a similar post-processing application) to a whole number
aspect ratio (e.g. 4:1 if you want 4 images) and then exporting the file with
the short edge dimension set to a nice even number (e.g. 2000px).

Once you have the individual photos on Instagram, applying a filter will
generally ruin the seamless effect (especially if you're using a vignette), so
try to do all your post-processing on the source image.

# Thanks
I got the idea for the script
from [Easton Chang](https://www.instagram.com/eastonchang/) (he's probably not
the first to take advantage of Instagram's seamless galleries in order to
display wider pictures, but he's the first person I noticed doing it), so check
him out to see some really cool photos!

Obviously, the bulk of the heavy lifting is being done by ImageMagick, so a big
thanks to them as well.
