from os import listdir, path, remove
from zipfile import ZipFile, is_zipfile

def main():
    # Get directory of this script.
    dirPath = path.dirname(path.realpath(__file__))

    unzipFiles(dirPath)

def unzipFiles(dirPath):
    for item in listdir(dirPath):
        if is_zipfile(item):
            with ZipFile(item) as f:
                f.extractall()
            remove(item)

if __name__ == "__main__":
    main()