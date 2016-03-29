# fitness-data-lake
Main project for a general health data lake development platform

This current project is a POC for development of a platform that gathers general health data from a variety of sources such as iPhones and FitBits. This uses vagrant and ansible to create and configure an ubuntu server with all necessary components for application development. The development environment is an Ubuntu/trusty64 vm running in VirtualBox

prerequisites:
	* install vagrant locally
	* install virtualbox locally (hypervisor for ubuntu vm)
	* install ansible locally
  * copy this repo locally

usage:
cd <directory where you copied this repo>/fitness-data-lake --> for example, /Projects/fitness-data-lake, if the repo is in /Projects
vagrant up --provider=virtualbox
