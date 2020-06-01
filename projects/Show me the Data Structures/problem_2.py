# Locally save and call this file ex.py ##
# Code to demonstrate the use of some of the OS modules in python

import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if not os.path.isdir(path):
        print(F"Not a valid directory path: {path}")
        return []

    if suffix is None or len(suffix) == 0 or suffix.isnumeric():
        print(F"This is not a valid suffix: {str(suffix)}")
        return []

    files_found = []
    for f in os.listdir(path):
        if os.path.isfile(path + f):
            if f.endswith(suffix):
                files_found.append(path + f)
        else:
            files_found += find_files(suffix, path + f + '/')
    return files_found


if __name__ == '__main__':
    path = 'testdir/'
    print(find_files('.h', path))  # returns a list of files ending in .h extension
    print(find_files('.c', path))  # returns a list of files ending in .c extension
    print(find_files('.op', path))  # returns an empty list
    print(find_files('', path))  # returns an empty list along a message: this is not a valid sufix
