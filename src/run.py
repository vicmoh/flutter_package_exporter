# This file contains the main function.
# that runs this program.

from flutter_library_exporter import FlutterLibraryExporter
import sys as _sys

FILE = _sys.argv[1]
SRC = _sys.argv[2]
OUT = _sys.argv[3]


def main():
    print('Script running...\n')
    FlutterLibraryExporter(FILE, SRC, OUT)
    print('\nScript complete.')


main()
