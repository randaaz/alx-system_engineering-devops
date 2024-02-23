# 0x0A Configuration Management
 
## Background Context

During work at SlideShare, an incident with an auto-remediation tool called Skynet occurred. A bug in the code led to unintended shutdowns of servers. Thanks to Puppet, the infrastructure was restored efficiently. This project emphasizes the importance of configuration management tools like Puppet.

## Requirements

### General
- All files interpreted on Ubuntu 20.04 LTS
- Files end with a new line
- `README.md` file at the root of the folder is mandatory
- Puppet manifests pass `puppet-lint` version 2.1.1 without errors
- Puppet manifests run without error
- First line of Puppet manifests is a comment explaining its purpose
- Puppet manifests files end with the extension `.pp`

## Tasks 
- 3 tasks
### Note on Versioning
Your Ubuntu 20.04 VM should have Puppet 5.5 preinstalled.

Install puppet
```bash
$ apt-get install -y ruby=1:2.7+1 --allow-downgrades
$ apt-get install -y ruby-augeas
$ apt-get install -y ruby-shadow
$ apt-get install -y puppet

