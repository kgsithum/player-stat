# Player Stats - Programming Task - OneReg

This project was created in Django.


## The task

The task is to create a small application using Django.

## Tech

- Django
- JQuery
- Bootstrap
- MySql

## Installation

Developed environment:  `Python >= 3.10.8` and `pip >= 22.3.1`. 

Install MySql server on localhost

```sh
sudo apt install mysql-server
ppip install mysqlclient
```
Reference: [Creating a Django App with MySql](https://www.cloudsigma.com/creating-a-django-app-with-database-connection-a-tutorial/)

To install the project, run:

```sh
cd player-stat
python manage.py runserver
```

Run migrations:

```sh
python manage.py migrate
```

## Features

- View all players.
- Load single player details.
- Create new player
- View all Grounds.
- Create a new ground.
- View all cities.
- Create a new city.

## Improvements

- Create new module to create stats and games.
- Create unit tests.
- Better user interface.
- Convert backend as a REST API.
- Create frontend using ReactJS.
