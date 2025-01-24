#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of web_static folder
using the function do_pack()
"""
from fabric.api import local
from datetime import datetime
import os

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
