# ASTOR

Online Algorithm Store
- based on `Python3.x` and `Django3.x`

The project uses the API provided by Django, and the admin system is Django's automatic admin system django-admin.

## Online Instance：

### Online Address

[https://astor.eveneko.com](https://astor.eveneko.com)

Account：student

Password：student

### Administrator

[https://astor.eveneko.com/admin](https://astor.eveneko.com/admin)

Account：student

Password：student


## Installation：

### Dependency
After downloading the project directory, use pip to install the dependency packages.

`pip3 install -r requirements.txt`

### Database Configuration


Use a small database `sqlite` which is automatically created when we generate the `Django` project. 


You can also configure to use MySQL.


You can aqcuire the existing database we build：[db.sqlite](http://share.eveneko.com/db.sqlite3)

### Create Super User

Execute the command in terminal:

`./python manage.py createsuperuser`

Then enter the super user name and password.

### Run the project

Execute the command in terminal:

`./python manage.py runserver`

Open with a browser: `http://127.0.0.1/`,  then you can enter the normal user entrance.

Open with a browser: `http://127.0.0.1/admin` then you can enter the super user entrance.
