# SE Foundations - 0x14-mysql

This project focuses on MySQL setup, replication, and backup, along with database administration and web stack debugging.

## Learning Objectives
By completing this project, you should be able to:
- Explain the main role of a database
- Understand database replication and its purpose
- Recognize the importance of storing database backups in different physical locations
- Perform regular operations to ensure the effectiveness of database backup strategy

## Tasks
### 0. Install MySQL
Install MySQL 5.7.x on both web-01 and web-02 servers. Ensure completion of SSH project task #3 on both servers.

### 1. Let us in!
Create a MySQL user named `holberton_user` on both servers with localhost host name and password `projectcorrection280hbtn`. Grant necessary permissions for checking primary/replica status.

### 2. If only you could see what I've seen with your eyes
Create a database named `tyrell_corp` on web-01 with a table `nexus6`. Add at least one entry to the table. Ensure `holberton_user` has SELECT permissions on the table.

### 3. Quite an experience to live in fear, isn't it?
Create a new user `replica_user` on web-01 for the replica server with appropriate permissions to replicate primary MySQL server. Grant SELECT privileges to `holberton_user` on `mysql.user` table.

### 4. Setup a Primary-Replica infrastructure using MySQL
Set up replication between web-01 (primary) and web-02 (replica) for the `tyrell_corp` database. Provide MySQL primary and replica configurations.

### 5. MySQL backup
Write a Bash script to generate a MySQL dump containing all databases, compress it to a tar.gz archive with the format `day-month-year.tar.gz`. The script should accept the MySQL root password as an argument.

## Repository Information
- GitHub Repository: [alx-system_engineering-devops](https://github.com/alx-system_engineering-devops)
- Directory: 0x14-mysql

