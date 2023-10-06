#!/usr/bin/python3
"""fabricscript to distribute an
archive to web servers using the function do_deploy.
"""

from fabric.api import env, put, run, sudo
from os.path import exists
import os

env.hosts = ["54.165.106.79", "100.25.109.126"]
env.user = "ubuntu"


def do_deploy(archive_path):
    """
    Distributes an archive to web servers and deploys it.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
