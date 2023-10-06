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
	arch_name = archive_path.split("/")[-1]
        no_ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run("mkdir -p {}{}/".format(path, no_ext))
        run("tar -xzf /tmp/{} -C {}{}/".format(arch_name, path, no_ext))
        run("rm /tmp/{}".format(arch_name))
        run("mv {0}{1}/web_static/* {0}{1}/".format(path, no_ext))
        run("rm -rf {}{}/web_static".format(path, no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{}/ /data/web_static/current".format(path, no_ext))

        return True
    except Exception as e:
        return False
