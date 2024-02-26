# 0x0D. Web stack debugging #0

## Overview
DevOps, SysAdmin, Scripting project for Holberton School. Weight: 1.

## Installing Docker
For this project, you will be given a container. If you want to install Docker locally, instructions are provided for Mac OS, Windows, Ubuntu 14.04, and Ubuntu 16.04.

## Requirements
- Allowed editors: vi, vim, emacs
- Files interpreted on Ubuntu 14.04 LTS
- All files should end with a new line
- README.md file is mandatory
- All Bash script files must be executable
- Bash scripts must pass Shellcheck without any error
- Bash scripts must run without error
- The first line of all Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all Bash scripts should be a comment explaining what the script is doing

## Tasks
### Task 0: Give me a page! (mandatory)
In this first debugging project, you need to get Apache to run on the container and return a page containing Hello Holberton when querying the root of it.

Example:

```bash
docker run -p 8080:80 -d -it holbertonschool/265-0
curl 0:8080
