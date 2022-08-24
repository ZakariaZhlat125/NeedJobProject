# NeedJobproject 
## django job protal
An open source online job portal using django==4.0.4

## Setup


[Download python-3.10.2](
   https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe
)

open thww terminal and run this :

Create virtual envvironment 
```
pip install virtualenv
virtualenv env
```
Activate env 
```
env\Scripts\Activate
```
install requirements
```
pip install -r requirements.txt
```
make migrations

```
python manage.py makemigrations
```
migrate database

```
python manage.py migrate
```

run server
```
python manage.py runserver`
```
