#! /usr/bin/env python3

import os
import monitor.varslist as v
import zipfile


def win_archive_report():
    """
    Change to the directory where the contents to archive reside.

    Print Current Directory.

    Archive and compression of the generated report file.

    Exit of the archiving process.

    Done using zipfile library
    :return:
    """
    os.chdir(v.win_dir)     # Changing to directory holding generated report.
    print('Current directory is: ' + os.getcwd())   # Printing current directory.
    win_archive_name = ('report_' + v.d_date_report_filename + '-' + v.d_time_report_filename)      # Assigning variable
    # for the name of the archive.
    file_to_archive = v.win_report_file_explicit        # Assigning variable for the file that needs to be archived.
    win_archive_proc = zipfile.ZipFile(v.win_dir + win_archive_name + '.zip', "w")      # variable for archive process.
    win_archive_proc.write(file_to_archive, compress_type=zipfile.ZIP_DEFLATED)     # performing archival.
    win_archive_proc.close()    # Exit from archive process.


def nix_archive_report():
    """
    Change to the directory where the contents to archive reside.

    Print Current Directory.

    Archive and compression of the generated report file.

    Exit of the archiving process.

    Done using zipfile library
    :return:
    """
    os.chdir(v.nix_dir)     # Changing to directory holding generated report.
    print('Current directory is: ' + os.getcwd())   # Printing current directory.
    nix_archive_name = ('report_' + v.d_date_report_filename + '-' + v.d_time_report_filename)      # Assigning variable
    # for the name of the archive.
    file_to_archive = v.nix_report_file_explicit        # Assigning variable for the file that needs to be archived.
    nix_archive_proc = zipfile.ZipFile(v.nix_dir + nix_archive_name + '.zip', "w")      # variable for archive process.
    nix_archive_proc.write(file_to_archive, compress_type=zipfile.ZIP_DEFLATED)     # performing archival.
    nix_archive_proc.close()    # Exit from archive process.
