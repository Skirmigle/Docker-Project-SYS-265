
## Initial Instalation:

1. Install the files using `git clone https://github.com/<you>/Docker-Project-SYS-265`
then access the file network using `cd Docker-Project-SYS-265/todo-api`

2. Once the files are installed, be sure to change all passwords in the .env file (POSTGRES_PASSWORD, ADMIN_PASSWORD, etc.).

3. After all files have been installed, enter `docker-compose up` This should start the webserver if docker and docker-compose are installed properly.

4. next join the website via `https://127.0.0.1:8000/docs`.


## Trouble Shooting:

If the service ever fails to boot, try the following:

1. `docker-compose down`
2. `docker system prune -f`

and then attempt to boot again.

If this does not work, make sure you have a recent enough version of docker and docker-compose installed, to check execute the following:

1. `docker --version`
2. `docker-compose --version`

If either of these are a version before those in system requirements, install a later verion and try again.


## System Requirements:

This software requires docker engine v 17.06.0 or higher be installed.

This software requires docker-compose v 2.0.0 or higher be installed.
