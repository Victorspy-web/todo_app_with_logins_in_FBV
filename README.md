# Dictionary App

This a Todo list app with logins using function based view

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing
purposes.

**Prerequisites**

```
Check requirements.txt for packages to install
```

**Installations**

```
First clone the repository from Github and switch to the project directory
```

* git clone git@github.com/USERNAME/{{ project_name }}.git

```
Open terminal and install pipenv for your project
```

`
You can use any other way of creating a virtual env if you are familiar with venvs
`

* sudo apt install pipenv

```
Install Django, activate and migrate project
```

* pipenv install django==3.2 . `Dont forget the space and dot at the end!`
* pipenv shell
* pip install PyDictionary
* python manage.py makemigrations
* python manage.py migrate

```
Create django superuser
```

* python manage.py createsuperuser
    * Fill in the fields to create a superuser `Passwords are invisble`

```
You can now run the development server
```

* python manage.py runserver
    * `Paste this link in your browser to run local server` http://127.0.0.1:8000