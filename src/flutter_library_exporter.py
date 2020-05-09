# This file contains the flutter library exporter
# which uses the file lister and writes out the
# file name.

from file_lister import FileLister
import re as _regex


class FlutterLibraryExporter:
    @staticmethod
    def export_string(file_name):
        return 'export \'' + _regex.sub(r"../src/", r"./src/", str(file_name)) + '\';'

    def __init__(self, file_name, src='../src/', out='../'):
        """Export and creates an export dart file based on the file 
        libraries under the [src] folder.
        @param src: is the path files to be exported.
        @param out: is the path of the [file_name].dart file to be outputed.
        @param file_name: excluding the [.dart] extension. Do not
        include the extension."""
        if (file_name is None or file_name == ''):
            file_name = 'exporter'
        if (src is None or src == ''):
            src = '../src/'
        if (out is None or out == ''):
            out = '../'
        super().__init__()
        f = open(out + str(file_name) + '.dart', "w+")
        fileLister = FileLister(
            dir_path_str=src,
            file_callback=FlutterLibraryExporter.export_string)
        string_to_write = 'library ' + \
            str(file_name) + ';\n\n' + str(fileLister.list_files())
        print(string_to_write)
        f.write(string_to_write)

