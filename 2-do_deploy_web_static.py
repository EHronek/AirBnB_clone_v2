#!/usr/bin/python3
"""distributes an archive to your web server, using
function do_deploy
Return:- false if the file at the path archive_path doesn't exit"""
from fabric.api import *
import os.path

env.user = "ubuntu"
env.hosts = ["52.3.247.198", "54.86.157.210"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """"distributes archive to web server"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        arc_file = archive_file.split(".")[0]
        decompress_location = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        sudo(f"mkdir -p {decompress_location}{arc_file}")
        target_loc = "/data/web_static/releases/{}".format(arc_file)
        sudo(f"tar -xzf /tmp/{archive_file} -C {target_loc}")
        sudo(f"rm /tmp/{archive_file}")
        sudo(f"mv {target_loc}/web_static/* {target_loc}/")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -s {target_loc}/ '/data/web_static/current'")
        return True
    except Exception as e:
        return False
