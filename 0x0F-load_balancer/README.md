# 0x0F. Load Balancer

## Background Context

You have been given 2 additional servers.

Let’s improve our web stack so that there is redundancy for our web servers. This will allow us to accept more traffic by doubling the number of web servers and make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Requirements

### General

- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 16.04 LTS
- All your files should end with a new line
- A README.md file, at the root of the folder of the project, is mandatory
- All your Bash script files must be executable
- Your Bash script must pass Shellcheck (version 0.3.7) without any error
- The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
- The second line of all your Bash scripts should be a comment explaining what the script is doing

## Tasks

### 0. Double the number of webservers

**Requirements:**

- Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02).
- The name of the custom HTTP header must be X-Served-By.
- The value of the custom HTTP header must be the hostname of the server Nginx is running on.
- Write 0-custom_http_response_header to configure a brand new Ubuntu machine to the requirements asked in this task.
- Ignore SC2154 for shellcheck.

### 1. Install your load balancer
**Requirements:**

Install and configure HAproxy on your lb-01 server.
Configure HAproxy to send traffic to web-01 and web-02.
Distribute requests using a round-robin algorithm.
Make sure HAproxy can be managed via an init script.
Make sure your servers are configured with the right hostnames: [STUDENT_ID]-web-01 and [STUDENT_ID]-web-02.

### advanced tasks
- 1 advanced task

