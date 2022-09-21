#!/usr/bin/env python3
"""A simple script to move two files into ceph_storage/
    Alta3 Research"""

# standard library imports
import shutil # shell utlities will be used to move files
import os # provides access to low level os operations


def main():
    """called at runtime"""

    # script will start in the home user directory (move us into this directory)
    os.chdir('/home/student/mycode/')

    # move the file to ceph_storage. will rewrite if already exists
    shutil.move('raynor.obj', 'ceph_storage/')

    # prompt user for new name for the karrigan.obj
    xname = input('What is the new name for kerrigan.obj? ')

    # rename the karrigan.obj file
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main() # this calls our main function
