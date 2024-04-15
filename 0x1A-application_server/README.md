# 0x1A. Application server

## Description
This project focuses on setting up an application server to serve dynamic content for an Airbnb clone project. The tasks involve configuring Nginx, setting up Gunicorn, and deploying Flask applications.

## Background Context
Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project, you will add this piece to your infrastructure, plug it into your Nginx, and make it serve your Airbnb clone project.


## Requirements
- Python 3 should be used for everything Python-related.
- All config files must have comments.
- Bash scripts should be executable and pass Shellcheck without any errors.
- Servers are running Ubuntu 16.04 LTS.

## Tasks
### 0. Set up development with Python
- Ensure completion of task #3 of your SSH project for web-01.
- Install the net-tools package on web-01.
- Git clone your AirBnB_clone_v2 on web-01.
- Configure the file web_flask/0-hello_route.py to serve its content from the route /airbnb-onepage/ on port 5000.
  
### 1. Set up production with Gunicorn
- Install Gunicorn and any required libraries.
- Serve content from the same route as in task 0 using Gunicorn on port 5000.

### 2. Serve a page with Nginx
- Configure Nginx to serve your page from the route /airbnb-onepage/.
- Nginx should proxy requests to the process listening on port 5000.
  
### 3. Add a route with query parameters
- Configure Nginx to proxy requests to the route /airbnb-dynamic/number_odd_or_even/(any integer) to a Gunicorn instance listening on port 5001.
- Serve this page both locally and on its public IP on port 80.
  
### 4. Let's do this for your API
- Git clone your AirBnB_clone_v3.
- Setup Nginx so that the route /api/ points to a Gunicorn instance listening on port 5002.
- Serve this page both locally and on its public IP on port 80.
  
### 5. Serve your AirBnB clone
- Git clone your AirBnB_clone_v4.
- Serve content from web_dynamic/2-hbnb.py on port 5003.
- Setup Nginx so that the route / points to your Gunicorn instance.
- Serve static assets found in web_dynamic/static/.
