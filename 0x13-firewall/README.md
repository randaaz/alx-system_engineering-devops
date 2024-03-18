# 0x13. Firewall

## Description
This project focuses on implementing firewall configurations using `ufw` (Uncomplicated Firewall) on web servers to regulate incoming and outgoing traffic.

## Concepts
For this project, we expect you to look at this concept:
- Web stack debugging

## Background Context
Your servers without a firewall…

## Resources
Read or watch:
- [What is a firewall](https://en.wikipedia.org/wiki/Firewall_(computing))

## Tasks
### 0. Block all incoming traffic but
Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:
- Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
  - 22 (SSH)
  - 443 (HTTPS SSL)
  - 80 (HTTP)
- Share the ufw commands that you used in your answer file
### advanced tasks
- 1 advanced tasks
