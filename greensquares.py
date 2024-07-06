# See LICENSE for licensing information.

from git import Repo
import sys
import os
import shutil
from datetime import datetime
import uuid # we use this for the file content
from requests import post
from time import sleep
# We need the following environment variables:
# GIT_REPO - The Git Repo repository to clone locally
# GIT_LOCAL_DIR - The folder to store the local git repository (default: ./git_repository)
# GIT_MODIFIED_FILE - The file to update (to make commits to) (default: file.txt)
# GIT_COMMIT_INTERVAL - The amount of time between 'git commit'
# GIT_COMMIT_PREFIX - The prefix to use with `git commit` messags. (default: "gsplusplus: ")
def mkCommitMsg(msg):
    """Make the commit message with the correct prefix"""
    return "%s %s" % (os.getenv("GIT_COMMIT_PREFIX", "gsplusplus:"), msg)
    
def main() -> int:
    """Program Entrypoint Function
    Returns: `int` (Exit Code)"""
    # display a banner because, well, i like it, OK?
    # i guess a file isn't best but I don't really want it
    # in this file.
    with open("%s/banner.txt" % os.path.dirname(__file__), "r") as f:
        print(f.read())
    
    local_dir = os.getenv("GIT_LOCAL_DIR", "./git_repository")
    changed_file = os.getenv("GIT_MODIFIED_FILE", "file.txt")
    repository = os.getenv("GIT_REPO", None)

    sys.stdout.write("Hold on, verifying your configuration... ")
    if repository == None:
        sys.stdout.write("Hey!  The Git repository environment variable ($GIT_REPO) isn't set!\n")
        sys.stdout.write("Let's fix that: Just set that to the SSH (or HTTPS if you like that) clone link.\n")
        return 1
    if os.path.isdir(local_dir):
        sys.stdout.write("Folder '%s' exists, destroying it... " % local_dir)
        shutil.rmtree(local_dir)
        sys.stdout.write("done.\n")

    sys.stdout.write("done.\n")
    sys.stdout.write("Cloning local copy... ")
    repo = Repo.clone_from(os.getenv("GIT_REPO"), local_dir)
    sys.stdout.write("done.\n")
    os.chdir(local_dir)
    if not os.path.isfile("git_repository/file.txt"): # ensure the file does exist
        sys.stdout.write("The file to commit to (%s) doesn't exist. Making it... " % changed_file)
        with open(changed_file, "w") as f:
            f.write(str(uuid.uuid4()))
        repo.index.add(changed_file)
        repo.index.commit(mkCommitMsg("Add the file"))
        sys.stdout.write("done.\n")

    while True:
        d = datetime.now()
        dstr = f"[{d.month}/{d.day}/{d.year} - {d.hour}:{d.minute}:{d.second}]"
        sys.stdout.write(f"[{dstr}] Running a commit for your green square schemes... ")
        with open(changed_file, "a") as f:
            f.write("\n%s" % str(uuid.uuid4()))
        repo.index.add(changed_file)
        repo.index.commit(mkCommitMsg(f"Here be green squares. {d.month}/{d.day}/{d.year}"))
        sys.stdout.write("done.\n")
        sleep(5)
    return 0

# import run prevention
if __name__ == "__main__":    
    sys.exit(main())
