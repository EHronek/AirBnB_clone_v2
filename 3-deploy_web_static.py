#!/usr/bin/python3
"""Fabric script (based on the file 2-do_deploy_web_static.py) that creates and distributes an archive to your web servers, using the function deploy"""
from fabric.api import *
import os
from datetime import datetime

env.hosts = ['52.3.247.198', '54.86.157.210']
env.key_filename = "~/.ssh/id_rsa"

def do_pack():
    """Distributes archive to my web server"""
    if not os.path.exists("versions"):
        os.makedirs("versions")

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = f"versions/web_static_{timestamp}.tgz"
    local("mkdir -p versions")

    create_tar = local('tar -cvzf {} web_static'.format(archive_name))

    if create_tar.succeeded:
        return archive_name
    else:
        return None

def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        arc_no_ext = archive_file.split(".")[0]
        dec_path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(dec_path, arc_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_file, dec_path, arc_no_ext))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(dec_path, arc_no_ext))
        run('rm -rf {}{}/web_static'.format(dec_path, arc_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(dec_path, arc_no_ext))
        return True
    except:
        return False

def deploy():
    """creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
