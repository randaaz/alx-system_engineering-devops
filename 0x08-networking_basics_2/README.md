# 0x08. Networking Basics #1

## Overview
This project focuses on networking basics, covering essential concepts related to localhost, IP addresses, hosts file, network interfaces, and more. The goal is to provide a foundational understanding of these concepts.

man or help:
- ifconfig
- telnet
- nc
- cut

## Learning Objectives
At the end of this project, you should be able to explain the following without external assistance:

### General
- What is localhost/127.0.0.1
- What is 0.0.0.0
- What is /etc/hosts
- How to display your machine’s active network interfaces

## Copyright - Plagiarism
- You are expected to come up with solutions for the tasks yourself to meet the learning objectives.
- Plagiarism is strictly forbidden and will result in removal from the program.
- Do not publish any content of this project.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS
- All your files should end with a new line
- Mandatory README.md file at the root of the project folder
- All Bash script files must be executable
- Bash scripts must pass Shellcheck (version 0.7.0 via apt-get) without any errors
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing



## Tasks

### 0. Change your home IP

**Mandatory**

Write a Bash script (`0-change_your_home_IP`) that configures an Ubuntu server with the following requirements:

- `localhost` resolves to `127.0.0.2`
- `facebook.com` resolves to `8.8.8.8`

# 0x08. Networking Basics 2

## Task 1: Show Attached IPs

**Mandatory**

Write a Bash script (`1-show_attached_IPs`) that displays all active IPv4 IPs on the machine it's executed on.

**Advanced**
- 1 advanced tasks
