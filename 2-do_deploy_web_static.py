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
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web servers
        put(archive_path, "/tmp/")

        # Extract the archive to /data/web_static/releases/<archive filename without extension>
        archive_filename = os.path.basename(archive_path)
        release_folder = "/data/web_static/releases/{}".format(archive_filename.split(".")[0])
        sudo("mkdir -p {}".format(release_folder))
        sudo("tar -xzf /tmp/{} -C {}".format(archive_filename, release_folder))

        # Delete the uploaded archive from the /tmp/ directory
        sudo("rm /tmp/{}".format(archive_filename))

        # Delete the current symbolic link
        current_link = "/data/web_static/current"
        if exists(current_link):
            sudo("rm -f {}".format(current_link))

        # Create a new symbolic link to the new version
        sudo("ln -s {} {}".format(release_folder, current_link))

        return True
    except Exception as e:
        return False
