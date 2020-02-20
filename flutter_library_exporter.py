# This file contains the flutter library exporter
# which uses the file lister and writes out the
# file name.

from file_lister import FileLister


class FlutterLibraryExporter:
    @staticmethod
    def export_string(file_name):
        return 'export \'' + str(file_name) + '\''

    def __init__(self, file_name):
        """Export and creates an export dart file based on the file 
        libraries under the [src] folder.
        @param file_name: excluding the [.dart] extension. Do not
        include the extension."""
        super().__init__()
        f = open(str(file_name) + '.dart', "w+")
        fileLister = FileLister(
            dir_path_str='../src',
            file_callback=lambda file: FlutterLibraryExporter.export_string(file))
        string_to_write = 'library ' + \
            str(file_name) + ';\n' + str(fileLister.list_files()) + '\n'
        f.write(string_to_write)
