# This file check a sub directory and list the files
# with the all the path under the directory.
# For example it is used to create and export files for
# all the files in the list for creating Flutter packages
# to have one import.

import os as _os


class FileLister:
    dir_path_str = ''

    def __init__(self, dir_path_str='./', file_callback=lambda file: 'File: ' + file):
        """List all files in the directories.
        @param file_callback: A callback function that callbacks the file string.
        The callback should return a string."""
        super().__init__()
        self.dir_path_str = dir_path_str
        self.list_files(self.dir_path_str, file_callback=file_callback)

    def list_files(self, dir_path_str='./', file_callback=lambda file: 'File: ' + file):
        """List files in the subtree of the directories.
        @return: The string all the files based on the [file_callback]."""
        path = dir_path_str
        files = []
        to_be_return = ''
        # r=root, d=directories, f = files
        for r, d, f in _os.walk(path):
            for file in f:
                if '.dart' in file:
                    files.append(_os.path.join(r, file))
        for f in files:
            if file_callback is not None:
                to_be_return += str(file_callback(f)) + '\n'
        return to_be_return
