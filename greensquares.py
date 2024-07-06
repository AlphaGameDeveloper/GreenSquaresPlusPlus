# See LICENSE for licensing information.

from git import Repo
import sys
import os
import shutil
import uuid # we use this for the file content

# We need the following environment variables:
# GIT_REPO - The Git Repo repository to clone locally
# GIT_LOCAL_DIR - The folder to store the local git repository (default: ./git_repository)
def main() -> int:
    """Program Entrypoint Function
    Returns: `int` (Exit Code)"""
    # display a banner because, well, i like it, OK?
    # i guess a file isn't best but I don't really want it
    # in this file.
    with open("%s/banner.txt" % os.path.dirname(__file__), "r") as f:
        print(f.read())
    
    local_dir = os.getenv("GIT_LOCAL_DIR", "./git_repository")

    if os.path.isdir(local_dir):
        sys.stdout.write("Folder '%s' exists, destroying it... " % local_dir)
        shutil.rmtree(local_dir)
        sys.stdout.write("done.\n")

    sys.stdout.write("Cloning local copy... ")
    repo = Repo.clone_from(os.getenv("GIT_REPO"), local_dir)
    sys.stdout.write("done.\n")
    if not os.path.isfile("git_repository/file.txt"): # ensure the file does exist
        with open("git_repository/file.txt", "w") as f:
            f.write(str(uuid.uuid4()))
    
    return 0

# import run prevention
if __name__ == "__main__":    
    sys.exit(main())
