#!/usr/bin/env python3

import shutil
import os

def main():
    # start script in the home user directory
    os.chdir("/home/student/mycode/")

    # copy the file at the source to the destination
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire folder with shutil.copytree
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
