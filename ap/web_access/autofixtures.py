
from .models import Request
from autofixture import register, AutoFixture

""" web_access.autofixtures

Uses django-autofixture to generate random testing data.
(https://github.com/gregmuellegger/django-autofixture/)

Create test data using the loadtestdata command, for example:
$ django-admin.py loadtestdata web_access.request

(note: generate Users before generating TAs and Trainees)
"""

class RequestAutoFixture(AutoFixture):
    field_values = {
    }

register(Request, RequestAutoFixture)
