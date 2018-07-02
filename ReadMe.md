#Notes

#Setting up a django project.

External software requirements :

- XAMPP. (should run to use mysqlclient)

for a more detailed theory and explanation watch TraversyMedia's django crash course vid.

https://www.youtube.com/watch?v=D6esTdOLXh4&t=915s

(project name and variables used in this project is not accurately same with TM's project but are still mostly similar).

1. Python version still have issues with mysqlclient (maybe because mysqlclient
does not have support for 3.7 yet), so I recommend installing python version 3.6.6.

2. install virtual environment
    using pip :

        python pip install virtualenv
        python pip install virtualenvwrapper-win

3. starting/making a django project using CMD. (git bash has recorded  issues with python).
    (assume project folder is in D:\PythonProjs\)

 In proj directory, make virtual environment

    mkvirtualenv [NAME]

to select which virtual environment to use : workon [NAME]

4. installing django
        
        run command : 

        pip install django

        Afterwards, to create your django project perform this command.

        django-admin startproject [DJANGO PROJ NAME]

        After the project files are installed go over to your project directory
        and open the folder with your preferred text editor. (when using VS code, enter command  'code .').

        to run server, perform: python manage.py runserver.

5. Installing mysqlclient. 

For Python version 3.6.6 the working version of mysqlclient is 1.3.12.

        pip install mysqlclient==1.3.12

after installing, watch TraversyMedia's video in the section where he configures the database
configurations in setting.py file. After doing so proceed to migrate to database. do so by running : 

        python manage.py migrate

#note, if error 1045 encountered, try removing the password value in database configuration in settings.py.



that's it for setup! watch TraversyMedia's video to know how to use the Django Web Framework!


