# djattendance
---

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
