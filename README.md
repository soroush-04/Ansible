
# Ansible

Created 3 services httpd, rabbitMQ, postgreSQL. Made an Ansible inventory for monitoring these services and also wrote an Ansible playbook to verify installation, check disk, and check status on these services.

You can check installed Ansible version by using this command `ansible --version`. If you don't have ansible installed, be sure to install it by using brew package for mac systems following this command `brew install ansible` or following this [link's guide](https://docs.ansible.com/ansible/latest/installation_guide/installation_distros.html) for other operating systems. to this directory by using `cd "directory path"` command.
- 2-a: You can find the answer for this task here in the [inventory.yml](./Task2/inventory.yml).
- 2-b: At first you have to move to this directory by using `cd/"folder path"` command an then run these commands:
```shell
ansible-palybook -i ./inventory.yml -e action="verify_install" playbook.yml
```

```shell
ansible-playbook -i ./inventory.yml -e action="check-disk" playbook.yml
```
