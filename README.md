<h1 align="center">GreenSquares++</h1>
<p align="center">Docker container to get those nice green squares, AUTOMATICALLY! (manicial laughter)</p>

<h2>Configuration</h2>
<p>Configuration is done via these environment variables.</p>

**YOU WILL NEED A GITHUB PRIVATE KEY**.  Add it as a volume to `/root/.ssh/id_rsa` (Docker) or `~/.ssh/id_rsa`, or if you have your own thing that works, feel free to go with that.

* `GIT_REPO` - The SSH url for `git commit`. (**REQUIRED**)
* `GIT_MODIFIED_FILE` - The file to use to make the bogus commits.  This will be visible on the GitHub repository. (**OPTIONAL, RECOMMENDED**, default:`file.txt`)
* `GIT_COMMIT_INTERVAL` - The amount of time (in seconds) between commits.  (**OPTIONAL, RECOMMENDED**, default:`86400 (1 day)`)
* `DISCORD_NOTIFICATIONS_WEBHOOK` - The Discord webhook to use to send updates and notifications to. (**OPTIONAL, RECOMMENDED**)
* `GIT_COMMIT_PREFIX` - The prefix to use for git commits. (**OPTIONAL**, default:`gsplusplus:`)
* `GIT_LOCAL_DIR` - The folder to store the local cloned repository. (**OPTIONAL**, default:`./git_repository`)

<h2>Docker</h2>
<h3>Docker via the command line</h3>

`docker run -d --restart=unless-stopped -e GIT_REPO="git@github.com:Username/Repository.git" -v /path/to/your/identity/file:/root/.ssh/id_ALGO --name greensquaresplusplus alphagamedev/greensquaresplusplus:latest`

<h3>Docker Compose</h3>

```yaml
version: "3"

services:
    greensquares:
        image: alphagamedev/greensquaresplusplus:latest
        volumes:
            - "/path/to/id_rsa:/root/.ssh/id_rsa"
        environment:
            GIT_REPO: "git@github.com:username/repo.git"
```
