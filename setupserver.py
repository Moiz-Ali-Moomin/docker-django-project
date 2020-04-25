#! /bin/python3

import os
import getpass
import time

def cmd(para):
  os.system(para)
  time.sleep(3)
  print("\n")
  os.system("tput setaf 1")
  print("-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-Clearing the screen-_-_-_-__-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-")
  time.sleep(2)
  os.system("clear")


while True:
 os.system("tput setaf 3")
 print('''
 \t\t\t\t\t\tPress 1 to run Docker-compose up for building the images
 \t\t\t\t\t\tPress 2 to create a new project
 \t\t\t\t\t\tPress 3 to make migration
 \t\t\t\t\t\tPress 4 to create admin account
 \t\t\t\t\t\tPress 5 to edit settings.py file of your django project
 \t\t\t\t\t\tPress 6 to collect static
 \t\t\t\t\t\tPress 7 to connect to MySQl server
 \t\t\t\t\t\tPress 8 to run python django-server 
 \t\t\t\t\t\tPress 9 to run docker-compose down to shut-down docker process
 \t\t\t\t\t\tPress 10 to exit 
 ''')
 os.system("tput setaf 6")
 choice = input("Choose Below options to perfom tasks: ")


 if int(choice) == 1:
  cmd("sudo docker-compose up -d")
  
 elif int(choice) == 2:
  name = input("Name of your Project: ")
  cmd("sudo docker-compose run python3-setup django-admin.py startproject {} .".format(name))
  
 elif int(choice) == 3:
  cmd("sudo docker-compose run python3-setup ./manage.py migrate")
  
 elif int(choice) == 4:
  cmd("sudo docker-compose run python3-setup ./manage.py createsuperuser")

 elif int(choice) == 5:
  appname = input("Your Django project name: ")
  cmd("sudo vim source/{}/settings.py".format(appname))
  
 elif int(choice) == 6:
  cmd("sudo docker-compose run python3-setup ./manage.py collectstatic")
 
 elif int(choice) == 7:
  dbname = input("Enter database username: ")
  dbpass = getpass.getpass(prompt='Enter you password: ')
  cmd("sudo docker exec -it docker-django-project_db_1 mysql -u {0} -p{1}".format(dbname, dbpass))
  
 elif int(choice) == 8:
  cmd("sudo docker-compose run python3-setup ./manage.py runserver")
  
 elif int(choice) == 9:
  cmd("sudo docker-compose down")

 elif int(choice) == 10:
  exit()
  
 else:
  cmd("echo WRONG selection")
