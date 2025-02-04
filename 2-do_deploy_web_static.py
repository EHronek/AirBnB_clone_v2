#!/usr/bin/python3
"""
distributes an archive to your web server, using
function do_deploy
Return:- false if the file at the path archive_path doesn't exit
"""

from fabric.api import put, run, env
import os
env.hosts = ['52.3.247.198', '54.86.157.210']
# env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive_file = archive_path.split("/")[-1]
        arc_no_ext = archive_file.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, arc_no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(archive_file, path, arc_no_ext))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, arc_no_ext))
        run('rm -rf {}{}/web_static'.format(path, arc_no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, arc_no_ext))
        return True
    except Exception as e:
        return False
