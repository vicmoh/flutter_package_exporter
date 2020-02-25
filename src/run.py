# This file contains the main function.
# that runs this program.

from flutter_library_exporter import FlutterLibraryExporter
import sys as _sys

FILE_NAME = _sys.argv[1]


def main():
    print('Script running...')
    FlutterLibraryExporter(FILE_NAME)
    print('Script complete.')


main()
