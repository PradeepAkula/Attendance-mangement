# Attendance-mangement
Attendance management using html,css,javascript and python.(used pgadmin, django, postgre sql)

image image image image image image

Getting Started
Prerequisites
Make sure you have installed visual studio c++, python3, pip package installer, pgadmin4 and postgresql before running the project.

Installation
Clone the repo sh git clone {repository link}

Open the migrations in home folder of the project and delete all the migration files which are numbered.

Install postgresql and Pg-admin in your system.

Create a database in pg admin.

Update the database name and password in settings.py file of AMS folder to connect the database to our project.

Change the directory to the place where manage.py file is available.

Create a virtual environment

pip install virtualenvwrapper-win
mkvirtualenv 'name of your environment'
Work on the created environment

workon 'name of your environment'
Install the following pacakges using command prompt in the virtual environment

pip install django
pip install psycopg2
pip install face_recognition
pip install cmake
Create django migrations for database using the following commands

python manage.py makemigrations
python manage.py sqlmigrate home 0001
python manage.py migrate
Create a super user i.e, the admin

python manage.py createsuperuser

The command prompt will ask for the username and password for the admin.
enter the required details
Run the server and open the website at http://127.0.0.1:8000/ localhost

python manage.py runserver

Screenshots of the project running
Screenshot (122)

Screenshot (123)

Screenshot (124)

Screenshot (125)

Use Case Diagram
image

Class Diagram
uml Final class Diagram

Sequence Diagrams
LOGIN Sequence
Untitled

Time Table Access Sequence
ams tt sequence

Queries Sequence
WhatsApp Image 2021-10-26 at 12 27 26 PM

Marking Attendance Sequence
Sequence Diagram AMS (2)
