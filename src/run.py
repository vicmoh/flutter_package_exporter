# This file contains the main function.
# that runs this program.

from flutter_library_exporter import FlutterLibraryExporter
import sys as _sys

FILE = _sys.argv[1]
SRC = _sys.argv[2]


def main():
    print('FILE: ', FILE)
    print('SRC: ', SRC)
    print('Script running...\n')
    FlutterLibraryExporter(FILE, src=SRC)
    print('\nScript complete.')


main()
