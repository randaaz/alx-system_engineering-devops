# 0x12. Web stack debugging #2

## Description
This project focuses on debugging web stack configurations and permissions to enhance security and functionality. Tasks involve running software as another user and configuring Nginx to run as a less privileged user.

## Concepts
For this project, we expect you to look at this concept:
- Web stack debugging

## Requirements
### General
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- A README.md file at the root of the folder of the project is mandatory
- All your Bash script files must be executable
- Your Bash scripts must pass Shellcheck without any error
- Your Bash scripts must run without error
- The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
- The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks
### 0. Run software as another user
#### Description
The script should run the `whoami` command under the user passed as an argument.

#### Requirements
- Write a Bash script that accepts one argument
- The script should run the `whoami` command under the user passed as an argument
- Make sure to try your script by passing different users

### 1. Run Nginx as Nginx
#### Description
Fix the container so that Nginx is running as the `nginx` user and listening on all active IPs on port 8080.

#### Requirements
- Nginx must be running as `nginx` user
- Nginx must be listening on all active IPs on port 8080
- You cannot use `apt-get remove`
- Write a Bash script that configures the container to fit the above requirements
#### advanced
- 1 advanced tasks

