Getting Started with djattendance

You should already have Python and Postgres installed on your machine, if not do that now (remember google is your friend)

Now 'git clone' the djattendance repo, if you are not officially part of the project on github, then you might want to fork the repo so you can work on it yourself and then send pull requests to interact with the team.

Next you need virtualenv, unless this is the only python project you will ever work on on your machine (highly unlikely) this will create a clean environment for you to work on this project in where all your dependencies are isolated and do not affect any other projects on your machine.

To install virtualenv following their docs at http://www.virtualenv.org/en/latest/virtualenv.html#installation. They are clear and easy to follow. DO NOT simply pip install or easy_install virtualenv, READ THE DOCS.

After you have virtual env installed, setup your virtual environment by running 'virtualenv venv' in the root directory of this project (the use of venv as a name is preferential and is just the standard used in this project). Activate your environment with "source venv/bin/activate" and deactivate with "deactivate."

Activate your venv now. In your terminal you should see (venv) at the front of each line. Then cd into requirements and run "pip install -r dev.txt" and let it run to completion. After all that installs you will also have to install gunicorn, autofixture, braces, and django_reset (again google is your friend).

Now you should set up your postgres database. Download and install PGAdmin III and 'add a connection to a server.'
FILL IN PLEASE I FORGET THIS PART

Now you need to adjust the DJANGO_SETTINGS_MODULE so it knows which file to look at for settings (the project does not have a settings.py file). Type in 'export DJANGO_SETTINGS_MODULE=ap.settings.dev' 'dev' here can be replaced with 'local' or 'prod' according to what you're trying to do.

cd in to 'ap' and run 'python manage.py syncdb' and 'python manage.py runserver' and you should be good to go!

HEROKU DEPLOY

'git checkout devdeploy'
major differences from master branch
1. requirements.txt in root folder so heroku can recognize this as a django app
2. Procfile to tell heroku what to do
3. using prod.py as settings file

must go into .git/config and change url under [remote "heroku"] from heroku.com to heroku.ACCOUNT_NAME
	helpful stackoverflow post concerning this http://stackoverflow.com/questions/4663103/multiple-heroku-accounts
pushing from branch instead of master 'git push heroku BRANCH_NAME:master'