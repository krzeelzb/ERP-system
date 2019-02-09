# ERP-system

Installation and set up:
```
$ mkdir emka
$ cd emka
$ python3 -m venv myvenv
$ source myvenv/bin/activate
(myvenv) ~$ python -m pip install --upgrade pip
(myvenv) ~$ git clone https://github.com/mmamica/ERP-system.git
(myvenv) ~$ cd ERP-system
(myvenv) ~$ pip install -r requirements2.txt
(myvenv) ~$ cd emka_trans
(myvenv) ~$ python manage.py makemigrations
(myvenv) ~$ python manage.py migrate
(myvenv) ~$ python manage.py runserver

```
