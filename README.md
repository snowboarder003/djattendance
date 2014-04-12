# djattendance
---

Branch for the March 29th demo.
Sarah and Rebecca are working directly on this branch with the attendance/schedules, so **please do not merge into this branch unless it works.** Thank you.

## Summary
Djattendance is a rewrite of the original FTTA attendance server in Python/Django. It supports many internal functions of the FTTA, for both trainees and administrators, such as:
* Attendance
* Service Scheduling
* Life-studies
* Class Syllabi
* etc.

## Architecture
The original attendance server was based on a traditional LAMPstack. The new version is written in Python on top of the Django web framework (djangoproject.com) using Postgres and Nginx.

### Backend
Python/Django
Postgres
Gunicorn
Nginx

### Frontend
HTML5 Boilerplate
Bootstrap

### Misc. Libraries
Celery (using Redis)
Memcached (deployment only)


## Running djattendance
A more detailed guide to running djattendance on your local machine can be found in the wiki (coming soon).

0. have Python and Postgres installed
1. `git clone` the djattendance repo
2. `pip install -r requirements.txt` from the `/requirements` (recommended that you use `virtualenv`)
3. using django: `manage.py syncdb` and `manage.py runserver` (be sure to use the local settings)


## Loading Autofixtures

The autofixture module is included in the requirements for dev environment. 

The order is very important because of the relationships between models. 
To load random test data in the db:

python manage.py loadtestdata aputils.country:10 --settings=ap.settings.local
python manage.py loadtestdata aputils.city:10 --settings=ap.settings.local
python manage.py loadtestdata aputils.address:10 --settings=ap.settings.local
python manage.py loadtestdata aputils.emergencyinfo:10 --settings=ap.settings.local
python manage.py loadtestdata terms.term:4 --settings=ap.settings.local
<!-- python manage.py loadtestdata localities.locality:10 --settings=ap.settings.local -->
python manage.py loadtestdata teams.team:10 --settings=ap.settings.local
python manage.py loadtestdata houses.house:10 --settings=ap.settings.local
python manage.py loadtestdata rooms.room:10 --settings=ap.settings.local
<!-- python manage.py loadtestdata houses.bunk:10 --settings=ap.settings.local --> // not used
python manage.py loadtestdata dj.category:10 --settings=ap.settings.local
python manage.py loadtestdata dj.service:10 --settings=ap.settings.local
python manage.py loadtestdata dj.period:10 --settings=ap.settings.local

python manage.py loadtestdata accounts.user:20 --settings=ap.settings.local
python manage.py loadtestdata accounts.trainingassistant:10 --settings=ap.settings.local
python manage.py loadtestdata accounts.trainee:10 --settings=ap.settings.local

python manage.py loadtestdata aputils.vehicle:10 --settings=ap.settings.local