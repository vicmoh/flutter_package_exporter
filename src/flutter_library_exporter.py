# This file contains the flutter library exporter
# which uses the file lister and writes out the
# file name.

from file_lister import FileLister
import re as _regex


class FlutterLibraryExporter:
    @staticmethod
    def export_string(file_name, src_path):
        func = 'FlutterLibraryExporter.export_string(): '
        debug = False 
        file_strip = _regex.sub(r"[.]+/", r"./", str(file_name))
        export_string = 'export \'' + file_strip + '\';'
        if debug:
            print(func, 'file_name = ', file_name)
            print(func, 'file_strip = ', file_strip)
            print(func, 'export_string = ', export_string)
        return export_string

    def __init__(self, file_name, src='../src/', out='../'):
        """Export and creates an export dart file based on the file 
        libraries under the [src] folder.
        @param src: is the path files to be exported.
        @param out: is the path of the [file_name].dart file to be outputed.
        @param file_name: excluding the [.dart] extension. Do not
        include the extension."""
        func =  'FlutterLibraryExporter():'
        debug = False 
        if debug:
            print(func, 'src = ', src, ', out = ', out)
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
            file_callback=lambda val: FlutterLibraryExporter.export_string(val, src))
        string_to_write = 'library ' + \
            str(file_name) + ';\n\n' + str(fileLister.list_files())
        print(string_to_write)
        f.write(string_to_write)

