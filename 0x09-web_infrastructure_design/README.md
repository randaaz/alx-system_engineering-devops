# 0x09. Web Infrastructure Design

## Overview

This project focuses on designing a web infrastructure, covering concepts related to DNS, monitoring, web server, network basics, load balancer, and servers. The tasks involve creating diagrams and explanations for different web infrastructure setups.

## Concepts

The project expects understanding of the following concepts:

- DNS
- Monitoring
- Web Server
- Network basics
- Load Balancer
- Server

## Learning Objectives

Upon completion, you are expected to:

- Explain the web stack diagram with sysadmin/devops track projects
- Explain the purpose of each component
- Describe system redundancy
- Understand acronyms: LAMP, SPOF, QPS

## Copyright - Plagiarism

- Solutions must be created to meet learning objectives
- No content publication allowed
- Plagiarism is strictly forbidden and results in removal from the program

## Requirements

### General

- **README.md:** Mandatory for the project
- **Whiteboarding:** Provide diagrams for each task
- **Manual Review:** Screenshots required for each task
- **Whiteboarding Session:** Each task must be explained without computer or notes
- **Focus on Requirements:** Answer what is asked, avoid unnecessary details
- **Quiz Questions:** Complete the quiz successfully

## Tasks

### Task 0: Simple Web Stack

#### Requirements:

- Design a one server web infrastructure for www.foobar.com
- Components: 1 server, 1 Nginx web server, 1 application server, 1 codebase, 1 MySQL database
- Domain: foobar.com with www record pointing to IP 8.8.8.8
- Explain: server, domain name, DNS record, web server, application server, database
- Issues: SPOF, downtime during maintenance, scalability challenges

#### URLs:

- **Repo:** [GitHub Repository](#)
- **Directory:** 0x09-web_infrastructure_design
- **File:** 0-simple_web_stack

### Task 1: Distributed Web Infrastructure

#### Requirements:

- Design a three-server web infrastructure for www.foobar.com
- Components: 2 servers, 1 Nginx web server, 1 application server, 1 HAproxy load balancer, 1 codebase, 1 MySQL database
- Explain: additional elements, load balancer distribution algorithm, Active-Active/Active-Passive setup, Primary-Replica cluster
- Issues: SPOF, security, no firewall, no HTTPS, no monitoring

#### URLs:

- **Directory:** 0x09-web_infrastructure_design
- **File:** 1-distributed_web_infrastructure

### Task 2: Secured and Monitored Web Infrastructure

#### Requirements:

- Design a three-server web infrastructure for www.foobar.com with security, encrypted traffic, and monitoring
- Components: 3 firewalls, SSL certificate for HTTPS, 3 monitoring clients
- Explain: purpose of additional elements, SSL termination issue, MySQL server write capacity issue, server uniformity problem
- Issues: SSL termination at load balancer, single writable MySQL server, server uniformity

#### URLs:

- **Directory:** 0x09-web_infrastructure_design
- **File:** 2-secured_and_monitored_web_infrastructure
