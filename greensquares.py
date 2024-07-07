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
# DISCORD_NOTIFICATIONS_WEBHOOK - discord webhook for notifications and info
def mkCommitMsg(msg):
    """Make the commit message with the correct prefix"""
    return "%s %s" % (os.getenv("GIT_COMMIT_PREFIX", "gsplusplus:"), msg)

def webhook(message):
    webhook = os.getenv("DISCORD_NOTIFICATIONS_WEBHOOK", None)
    useWebhook = (webhook != None)

    if useWebhook:
        post(webhook, {
            "content": "**[ :green_square:++ ]** %s" % message
        })

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
    webhookUrl = os.getenv("DISCORD_NOTIFICATIONS_WEBHOOK", None)
    useWebhook = (webhookUrl != None)
    prefix = os.getenv("GIT_COMMIT_PREFIX", None)
    commitInterval = os.getenv("GIT_COMMIT_INTERVAL", 86400)
    
    sys.stdout.write("Hold on, verifying your configuration...\n")

    # ----- NO REPOSITORY SET -----
    if repository == None:
        sys.stdout.write("Hey!  The Git repository environment variable ($GIT_REPO) isn't set!\n")
        sys.stdout.write("Let's fix that: Just set that to the SSH (or HTTPS if you like that) clone link.\n")
        return 1

    # ----- WILL A WEBHOOK BE USED? -----
    sys.stdout.write("Checking if a Discord webhook will be used... ")
    sys.stdout.write("yes.\n" if useWebhook else "no.\n")

    # ----- CUSTOM GIT PREFIX -----
    sys.stdout.write("Checking if a custom Git commit prefix will be used... ")
    sys.stdout.write(
        "yes. (%s)\n" % prefix if prefix != None else "no.\n"
    ) 


    # ----- SHOW GIT REPO -----
    sys.stdout.write("Checking Git Repository... ")
    sys.stdout.write("%s\n" % repository)

    # ----- CHECK IF COMMIT INTERVAL IS OK -----
    sys.stdout.write("Checking if $GIT_COMMIT_INTERVAL is valid... ")
    try:
        commitInterval = int(commitInterval)
    except ValueError:
        sys.stdout.write("no. (Can't be converted to an integer)\n")
        return 1

    if commitInterval < 0:
        sys.stdout.write("no. (Number is negative)\n")
        return 1
    sys.stdout.write("ok.\n")

    # ----- CHECK IF GIT_LOCAL_DIR EXISTS -----
    sys.stdout.write("Checking if $GIT_LOCAL_DIR already exists... ")
    if os.path.isdir(local_dir):
        sys.stdout.write("yes.\n")
        sys.stdout.write("Folder '%s' exists, destroying it... " % local_dir)
        shutil.rmtree(local_dir)
        sys.stdout.write("done.\n")
    else:
        sys.stdout.write("no.\n")

    # ----- CONFIG OK -----
    sys.stdout.write("Configuration OK.\n")
    
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

    webhook("GreenSquares++ has started!")
    
    while True:
        d = datetime.now()
        dstr = f"[{d.month}/{d.day}/{d.year} - {d.hour}:{d.minute}:{d.second}]"
        sys.stdout.write(f"[{dstr}] Running a commit for your green square schemes... ")
        with open(changed_file, "a") as f:
            f.write("\n%s" % str(uuid.uuid4()))
        repo.index.add(changed_file)
        repo.index.commit(mkCommitMsg(f"Here be green squares. {d.month}/{d.day}/{d.year}"))
        sys.stdout.write("done.\n")
        webhook("Commit OK")
        sleep(commitInterval)

    return 0

# import run prevention
if __name__ == "__main__":    
    sys.exit(main())
