# This file check a sub directory and list the files
# with the all the path under the directory.
# It is used to create an export files for all the files in the
# list for creating Flutter packages to have one import.

import os as _os
import sys as _sys

PATH = _sys.argv[0]


class FileLister:
    dirPathStr = ''

    @staticmethod
    def flutterExport(filePathStr):
        print('export \'' + filePathStr + '\'')

    def __init__(self, dirPathStr='./', fileCallback=lambda file: print(file)):
        super().__init__()
        self.dirPathStr = dirPathStr
        self.listFilesInDir(self.dirPathStr, fileCallback=fileCallback)

    def listFilesInDir(self, dirPathStr='./', fileCallback=lambda file: print(file)):
        """List files in the subtree of the directories."""
        path = dirPathStr
        files = []
        # r=root, d=directories, f = files
        for r, d, f in _os.walk(path):
            for file in f:
                if '.dart' in file:
                    files.append(_os.path.join(r, file))
        for f in files:
            if fileCallback is not None:
                fileCallback(f)


def main():
    print('Script running...')
    FileLister(PATH, fileCallback=FileLister.flutterExport)
    print('Script complete.')


main()
