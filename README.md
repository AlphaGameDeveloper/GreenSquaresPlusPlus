<h1 align="center">GreenSquares++</h1>
<p align="center">Docker container to get those nice green squares, AUTOMATICALLY! (manicial laughter)</p>

<h2>Configuration</h2>
<p>Configuration is done via these environment variables.</p>

* `GIT_REPO` - The SSH url for `git commit`. (**REQUIRED**)
* `GIT_MODIFIED_FILE` - The file to use to make the bogus commits.  This will be visible on the GitHub repository. (**OPTIONAL, RECOMMENDED**, default:`file.txt`)
* `GIT_COMMIT_INTERVAL` - The amount of time (in seconds) between commits.  (**OPTIONAL, RECOMMENDED**, default:`86400 (1 day)`)
* `DISCORD_NOTIFICATIONS_WEBHOOK` - The Discord webhook to use to send updates and notifications to. (**OPTIONAL, RECOMMENDED**)
* `GIT_COMMIT_PREFIX` - The prefix to use for git commits. (**OPTIONAL**, default:`gsplusplus:`)
* `GIT_LOCAL_DIR` - The folder to store the local cloned repository. (**OPTIONAL**, default:`./git_repository`)
