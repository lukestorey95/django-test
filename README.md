```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip

pip install django
pip install djangorestframework

django-admin startproject backendAPI
cd backendAPI

python manage.py runserver
python manage.py startapp backend

python manage.py createsuperuser

python manage.py makemigrations
python manage.py migrate


```