# 0x0B. SSH

## DevOps, SSH, Network, SysAdmin, Security
**By: Sylvain Kalache**
Weight: 1
Project started on Feb 23, 2024 6:00 AM and must end by Feb 26, 2024 6:00 AM
Checker released at Feb 24, 2024 12:00 AM
Auto review will be launched at the deadline

## Background Context
...
... (Content truncated for brevity)
...

### 0. Use a private key
```bash
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to [Your Server IP] closed.
sylvain@ubuntu$

### 1. Create an SSH key pair
bash
Copy code
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
###1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$
Repo: 0x0B-ssh/1-create_ssh_key_pair

### 2. Client configuration file
bash
Copy code
sylvain@ubuntu$ ssh -v ubuntu@[Your Server IP]
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
[Debug Information]
Authenticated to [Your Server IP] ([Your Server IP]:22).
[Debug Information]
ubuntu@magic-server:~$
Repo: 0x0B-ssh/2-ssh_config

###3. Let me in!
Now that you have successfully connected to your server, we would also like to join the party.
Add the SSH public key below to your server so that we can connect using the ubuntu user.

Copy code
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOT
