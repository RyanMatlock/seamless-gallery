# A simple example
Depending on where you have the script installed, you may be able to run
`seamlessgallery` as easily as

```
$ seamlessgallery /path/to/test.jpg
```

or you may have to run it like

```
$ python3 /different/path/to/seamlessgallery.py /path/to/test.jpg
```

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
(Again, when it comes to Windows, I'm basically clueless.)

Personally, I like keeping this project directory in a folder where I keep my
scripts (e.g. `~/misc-scripts/seamlessgallery`), then I symlink it to somewhere
on my `PATH` (to figure out which folders are on your path, simply enter

```
$ echo $PATH
```

to see
