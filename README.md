# Recruiter Exam System

Technolgoy We Used for this application:

* Django
* Django REST Framework
* ReactJS/Redux
* SASS
* Bootstrap


## A few very quick steps to run this app

## clone this repo

```
 git clone https://github.com/MySecondLanguage/RES.git
```

step into project directory

```
cd RES
```

## Backend Setup

We assume you have installed python3.x installed into your machine.

also we assume you have install pip3 latest version

if you don't have pip3, try these commands:

```
sudo apt-get update
sudo apt-get install python3-pip
```

if above commands not works, please google it and get the right command for your OS

### Setup virtualenv


```
 pip3 install virtualenv

```
Create a virtualenv
```
 virtualenv yourdesiredname
```

```
source yourdesiredname/bin/activate
```

### Install Dependency

```
pip3 install -r requirements.txt
```

## Frontend Setup

We assume you have installed npm or yarn

install dependecny

```
 npm install
```

build the file

```
 npm run build
```

for development purpose

```
 npm run watch
```

#### You almost there

run the django server

we assume you are in project directory (RES)

```
python3 backend/manage.py migrate
python3 backend/manage.py runserver
```

and create a superuser

```
python3 backend/manage.py createsuperuser
```

# or you can try with docker

```
 docker-compose up
```

# LICENSE
Disclaimer: Everything you see here is open and free to use as long as you comply with the license. We promise to do our best to fix bugs and improve the code.

#### Crafted with ❤️ by [Anamul Hoq](https://www.linkedin.com/in/pymamun/)

`Reach me over mail: `
mamun.py1 [at] gmail dot come

