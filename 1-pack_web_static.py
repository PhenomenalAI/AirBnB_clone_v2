#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Creates a .tgz archive from the contents of the web_static folder.
    """
    # Create the "versions" directory if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

    # Create the name of the archive file
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(timestamp)

    # Compress the web_static folder into a .tgz archive
    result = local("tar -cvzf {} web_static".format(archive_name))

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_name
    else:
        return None
