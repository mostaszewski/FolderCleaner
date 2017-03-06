"""
    A simple script to sort and move files by their extension
    Example usage: app.py C:\\Users\\Test\\Downloads
"""

from os import listdir, makedirs
from os.path import isfile, join, splitext
from shutil import move
from sys import argv

def get_files(path):
    """ Returns list of files in the specified directory """
    return [file for file in listdir(path) if isfile(join(path, file))]

def clean(paths):
    """
        Moves each file to a folder with file extension name.
        For example: "invoice.pdf" will be moved to "pdf" directory.
    """
    for path in paths:
        for file in get_files(path):
            _, extension = splitext(file)
            source = join(path, file)
            if extension == '':
                destination = join(path, "No extension")
            else:
                destination = join(path, extension.replace('.', ''))
            makedirs(destination, exist_ok=True)
            move(source, destination)
            print("Copying {} to {}.".format(source, destination))

if __name__ == "__main__":
    try:
        clean(argv[1:])
    except IndexError:
        print("You must provide at least one source directory!")
