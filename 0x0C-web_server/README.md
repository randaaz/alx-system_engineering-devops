# 0x0C. Web server

## Overview
DevOps, SysAdmin project for Holberton School by Sylvain Kalache. Weight: 1.

## Concepts
For this project, we expect you to look at this concept:
- What is a Child Process?

## Background Context
In this project, some tasks will be graded on 2 aspects:

1. Is your web-01 server configured according to requirements?
2. Does your answer file contain a Bash script that automatically performs commands to configure an Ubuntu machine to fit requirements (meaning without any human intervention)?

For example, if you need to create a file `/tmp/test` containing the string `hello world` and modify the configuration of Nginx to listen on port 8080 instead of 80, you can use `emacs` on your server to create the file and to modify the Nginx configuration file `/etc/nginx/sites-enabled/default`.

But your answer file would contain:

```bash
#!/usr/bin/env bash
# Configuring a server with specification XYZ
echo hello world > /tmp/test
sed -i 's/80/8080/g' /etc/nginx/sites-enabled/default

