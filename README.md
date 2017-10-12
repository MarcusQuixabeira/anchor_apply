  # Overseer

This application was developed as part of a selection process for a job. Its function is to validate credit card numbers informed through a .txt file from a set of defined rules.

## Prerequisites

1. Installed Python (https://wiki.python.org/moin/BeginnersGuide/Download)
2. Installed Django (https://docs.djangoproject.com/en/1.11/topics/install/)

### Installing

Clone this repository:
```
$ git clone git@github.com:MarcusQuixabeira/anchor_apply.git
```
Inside repository's folder make and run the migrations:
```
$ python manage.py makemigrations
$ python manage.py migrate
```
Create a super user to access admnistration area (https://docs.djangoproject.com/en/1.11/intro/tutorial02/#creating-an-admin-user)

Finally run the application:
```
$ python manage.py runserver
```

Access the application at http://localhost:8000 to validate a .txt file

Access the application at http://localhost:8000/admin to check the admininistration area

## Tests

Run the following command to run the testcase:
```
$ python manage.py test overseer
```

## Demo

A demo can be accessed at:

https://tranquil-crag-11048.herokuapp.com/

https://tranquil-crag-11048.herokuapp.com/admin (admin area)

Use the following credentials in the admin area:

username: fredrick

password: crazy_blagonga
