# Poor Man's Twitter - Django + Django Rest + VueJS app
pip install -r requirements.txt

### to run type
git clone https://github.com/hgmh3/ptwt.git
python manage.py runserver
access with your browser: http://127.0.0.1:8000

### to run tests:
python manage.py test

### to init database (optional)
python manage.py migrate

### to post data using curl, first (optional)
python manage.py createsuperuser
