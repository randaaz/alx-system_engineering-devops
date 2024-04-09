# Webstack Monitoring

This project involves setting up monitoring for a web stack using Datadog, a monitoring and analytics platform. Monitoring is essential for ensuring the reliability, performance, and availability of servers and applications.

## Background

Monitoring is crucial for identifying and addressing issues in real-time, optimizing performance, and making informed decisions about resource allocation and scaling. There are two main areas of monitoring:

1. **Application Monitoring:** Monitoring the behavior and performance of running software to ensure it meets expected standards and performance metrics.

2. **Server Monitoring:** Monitoring the resources and health of servers (virtual or physical) to prevent overloads and ensure optimal performance.

Access logs and error logs are essential components of web server monitoring:

- **Access Logs:** Records information about requests made to the web server, including details such as the IP address of the client, the requested resource, and the response status code.

- **Error Logs:** Records information about errors encountered by the web server, such as HTTP errors, server errors, and application errors.

## Tasks

### 0. Sign up for Datadog and install datadog-agent

- Sign up for a free Datadog account on the Datadog website, selecting statistics from your current stack for monitoring.
- Install the Datadog agent on the web-01 server.
- Create an application key.
- Provide your DataDog API key and application key in your Intranet user profile.
- Ensure that the web-01 server is visible in Datadog under the hostname XX-web-01.

### 1. Monitor some metrics

Set up monitors within the Datadog dashboard to monitor and alert you of the following system metrics:
- Number of read requests issued to the device per second.
- Number of write requests issued to the device per second.

### 2. Create a dashboard

Create a new dashboard in Datadog and add at least 4 widgets to visualize different metrics.

## Instructions

To set up monitoring and create the dashboard, follow the instructions provided in each task's directory.

## Author

This project is authored by Randa Saeed.


