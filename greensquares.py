# See LICENSE for licensing information.

from git import Repo
import sys
import os
import uuid # we use this for the file content

def main() -> int:
    """Program Entrypoint Function
    Returns: `int` (Exit Code)"""

    repo = Repo.clone_from(os.getenv("GIT_REPO_URL"), "git_repository")

    if not os.path.isfile("git_repository/file.txt"): # ensure the file does exist
        with open("git_repository/file.txt", "w") as f:
            f.write(str(uuid.uuid4()))
    
    return 0

# import run prevention
if __name__ == "__main__":
    sys.exit(main())
