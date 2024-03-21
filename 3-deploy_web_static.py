#!/usr/bin/python3
import os
from fabric.api import *
from datetime import datetime


env.hosts = ['100.26.122.8', '54.209.216.103']
env.user = 'ubuntu'


def do_pack():
    """compresses a directory and its content using fabric"""
    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz"
            .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    result = local("tar -cvzf {} web_static"
                   .format(path))

    if result.failed:
        return False
    return path


def do_deploy(archive_path):
    """Deploys the static files to the host servers.
    Args:
        archive_path (str): The path to the archived static files.
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p {}".format(folder_path))
        run("sudo tar xvzf /tmp/{0} -C {1}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("sudo mv {}web_static/* {}".format(folder_path, folder_path))
        run("sudo rm -rf {}web_static".format(folder_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success


def deploy():
    """Archives and deploys the web_static content to multiple
    remote servers"""

    path = do_pack()
    return do_deploy(path)
