import io
import os
import subprocess
import lzma

file_open = open


def reader(path):
    """
    Turns a path to a dump file into a file-like object of (decompressed)
    XML data assuming that '7z' is installed and will know what to do.

    :Parameters:
        path : `str`
            the path to the dump file to read
    """
    return lzma.open(path, "rt", encoding = "utf-8", errors = "replace")
