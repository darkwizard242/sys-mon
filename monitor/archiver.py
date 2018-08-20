#! /usr/bin/env python3

import os
import monitor.varslist as v


def win_archive_report():
    """
    Change to the directory where the contents to archive reside.

    Print Current Directory.

    Archive and compression of the generated report file.

    Exit of the archiving process.

    Done using zipfile library
    :return:
    """
    os.chdir(v.win_dir)
    print('Current directory is: ' + os.getcwd())
    v.archive_proc.write(v.file_to_archive, compress_type=v.zipfile.ZIP_DEFLATED)
    v.archive_proc.close()
