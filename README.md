
## Initial Instalation:

1. Install the files using `git clone https://github.com/<you>/Docker-Project-SYS-265`
then access the file network using `cd Docker-Project-SYS-265/todo-api`

2. Once the files are installed, be sure to change all passwords in the .env file (POSTGRES_PASSWORD, ADMIN_PASSWORD, etc.).

3. After all files have been installed, enter `docker-compose up` This should start the webserver if docker and docker-compose are installed properly.

4. next join the website via `https://127.0.0.1:8000/docs`.


## Application Use:

This application serves as a digital todo list, it has four important functions GET, POST, PUT, and DELETE.

1. GET: This is used to retreive the entire todo list, to execute this function opne the tab, press "try it out" and then press execute. This should print the list below it.
2. POST: This is used to add a new entry on the todo list, to execute this function opne the tab, press "try it out" and then fill the "string" value with your todo task and press execute. This should add a new entry to the todo list.
3. PUT: This is used to mark a entry as complete,  to execute this function opne the tab, press "try it out" and then enter the id of the entry (the number associated with it in the get output) and press execute. This shoul.d mark the entry as complete.
4. DELETE: This is used to remove an entry from the list, to execute this function opne the tab, press "try it out" and then enter the id of the entry (the number associated with it in the get output) and press execute. This should remove the entry.


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
