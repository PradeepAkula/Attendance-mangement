# Attendance-mangement
Attendance management using facial recognition for colleges,companies etc using html,css,javascript and python.(used pgadmin, django, postgre sql)

![image](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![image](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![image](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green) 
![image](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white) ![image](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white) ![image](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E) 

## Getting Started
### Prerequisites

Make sure you have installed *visual studio c++*, *python3*, *pip package installer*, *pgadmin4* and *postgresql* before running the project.

### Installation

* Clone the repo
   sh
   git clone {repository link}
   
* Open the migrations in home folder of the project(main AMS folder) and delete all the migration files which are numbered.
* Install postgresql and Pg-admin in your system.(install pgadmin seperately instead of including it in postgresql installation to avoid errors).
* Dont forget to install "Microsoft visual studio c++".(dont confuse with normal visual studio code)
* Create a database in pg admin.
* Update the database name and password in *settings.py* file of AMS folder inside the project(main AMS folder) to connect the database to our project.
* Change the directory to the place where manage.py file is available.
* Create a virtual environment
   * pip install virtualenvwrapper-win
   * mkvirtualenv 'name of your environment'
   
* Work on the created environment

   * workon 'name of your environment'
   
* Install the following pacakges using command prompt in the virtual environment
   
   * pip install django
   * pip install psycopg2
   * pip install cmake
   * pip install face_recognition
   
* Create django migrations for database using the following commands
   
   * python manage.py makemigrations
   * python manage.py sqlmigrate home 0001
   * python manage.py migrate
   
* Create a super user i.e, the admin using the command below
   
   python manage.py createsuperuser
  
   
   * The command prompt will ask for the username and password for the admin.
   * enter the required details.(the password will not be visible while entering,so please type the password and press enter for conforming,type again the same password, it will not be visible now also ,so please take care and hit enter.) 
   * Creating a superuser(admin) is necessary for a new database.
   * (Only in extreme case becuz it may create errors)If you dont create a new database then use admin details to use the existing database.
   * Username:prade
   * Password:prade 
   
* Run the server and open the website at http://127.0.0.1:8000/ localhost(run the command below to use the website)
   
   *python manage.py runserver
   
## Screenshots of the project running
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/Screenshot%20(254).png)

![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/Screenshot%20(255).png)

![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/Screenshot%20(256).png)

![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/Screenshot%20(258).png)

## Usecase Diagram

![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/usecase%20ams.png)

## Class Diagram
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/class%20ams.jpeg)

## Sequence Diagrams

### LOGIN Sequence
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/loginseq%20ams.png)

### Time Table Access Sequence
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/timetableseq%20ams.jpg)

### Queries Sequence
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/queriesseq%20ams.jpeg)

### Marking Attendance Sequence
![image](https://github.com/PradeepAkula/Attendance-mangement/blob/main/pictures%20ams/markattend%20ams.jpg)

