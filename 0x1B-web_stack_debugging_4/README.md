# 0x1B. Web stack debugging #4

## Description
This project focuses on debugging and optimizing a web server setup featuring Nginx under pressure. The goal is to fix issues causing a high number of failed requests and errors.

## Requirements
- All files are interpreted on Ubuntu 14.04 LTS.
- Puppet manifests must pass puppet-lint version 2.1.1 without any errors.
- Puppet manifests must run without error.
- Puppet manifests first line must be a comment explaining what the Puppet manifest is about.
- Puppet manifests files must end with the extension .pp.
- Files will be checked with Puppet v3.4.
- Install puppet-lint: `$ apt-get install -y ruby` followed by `$ gem install puppet-lint -v 2.1.1`.

## Tasks
### 0. Sky is the limit, let's bring that limit higher
- Simulate HTTP requests to a web server using ApacheBench.
- Benchmark the server and identify issues causing failed requests.
- Fix the stack to ensure 0 failed requests.

### 1. User limit
- Change the OS configuration to allow the holberton user to login and open a file without encountering errors.
