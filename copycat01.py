#!/usr/bin/env python3
""" Explore file manipulation"""

import shutil
import os

def main():

    os.chdir("/home/student/mycode/")
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")
    shutil.copytree("5g_research/", "5g_research_backup/")

main()
