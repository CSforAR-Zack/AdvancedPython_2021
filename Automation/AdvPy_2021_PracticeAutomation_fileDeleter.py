from os import path, listdir, remove

def main():
    # Get directory of this script.
    dirPath = path.dirname(path.realpath(__file__))

    fileDeleter(dirPath, "txt")

def fileDeleter(dirPath, ext):
    for file in listdir(dirPath):
        if file.endswith(f".{ext}"):
            remove(str(file))

if __name__ == "__main__":
    main()