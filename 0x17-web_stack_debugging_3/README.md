# Web Stack Debugging #3

This project involves debugging a Wordpress website running on a LAMP stack, where Apache is returning a 500 error. The goal is to use strace to identify the issue, fix it manually, and then automate the fix using Puppet.

## Background

Wordpress is a widely-used tool for running blogs, portfolios, e-commerce, and company websites, powering 26% of the web. It is typically run on a LAMP stack (Linux, Apache, MySQL, and PHP).

## Tasks

### 0. Strace is your friend

Using strace, the task is to find out why Apache is returning a 500 error, fix the issue manually, and then automate the fix using Puppet.

#### Requirements:

- The `0-strace_is_your_friend.pp` file must contain Puppet code.
- Any Puppet resource type can be used for the fix.

### Example:

```bash
$ curl -sI 127.0.0.1
HTTP/1.0 500 Internal Server Error
Date: Fri, 24 Mar 2017 07:32:16 GMT
Server: Apache/2.4.7 (Ubuntu)
X-Powered-By: PHP/5.5.9-1ubuntu4.21
Connection: close
Content-Type: text/html

$ puppet apply 0-strace_is_your_friend.pp

