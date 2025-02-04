#!/usr/bin/python3
"""
Script deletes out of date archives
"""
import os
from fabric.api import *

env.hosts= ['52.3.247.198', '54.86.157.210']


def do_clean(number=0):
    """ Deletes out of date archives depending on the number provide"""
    number = 1 if int(number) == 0 else int(number)

    archive_files = sorted(os.listdir("versions"))
    [archive_files.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(arch)) for arch in archive_files]
    with cd("/data/web_static/releases"):
        archive_files = run("ls -tr").split()
        archive_files = [arch for arch in archive_files if "web_static_" in arch]
        [archive_files.pop() for i in range(number)]
        [run("rm -rf ./{}".format(arc)) for arc in archive_files]

