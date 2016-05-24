# fitness-data-lake
Main project for a general health data lake development platform

This current project is a POC for development of a platform that gathers general health data from a variety of sources such as iPhones and FitBits. This uses vagrant and ansible to create and configure an ubuntu server with all necessary components for application development. The development environment is an Ubuntu/trusty64 vm running in VirtualBox

Acknowledgements:

Ansible roles were borrowed from https://galaxy.ansible.com/nkadithya31/ansible/, which contains many more ubuntu server roles.
The main fitbit API project comes from https://github.com/edrabbit/fitbitsplunk

Prerequisites:
This project uses vagrant and ansible in order to configure the ubuntu server. If you have a server with these tools installed, simply copy this repo to that server. If you don't have an environment, perform the steps below on a server/laptop. This was tested on a Mac running OS X 10.10.5.
  * install vagrant locally
  * install virtualbox locally (hypervisor for ubuntu vm)
  * install ansible locally
  * copy this repo locally

usage:

cd <directory where you copied this repo>/fitness-data-lake --> for example, /Projects/fitness-data-lake, if the repo is in /Projects

vagrant up --provider=virtualbox