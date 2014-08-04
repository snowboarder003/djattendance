
from django.db import models
from macaddress.fields import MACAddressField

from accounts.models import Trainee

""" web-access models.py
This module handles requests for Internet access either made by trainees or for
a guest by their MAC address.

REQUEST
    - This model represents a web-access request submitted by a trainee or
    guest.

"""


class Request(models.Model):

    TYPE_APPROVAL_STATUS_CHOICES = (
        ('Pn', 'Pending'),
        ('Ap', 'Approved'),
        ('Fs', 'Fellowship'),
        ('Dn', 'Denied'),
        ('Ex', 'Expired'),
    )

    TYPE_REASON_CHOICES = (
        ('Go', 'Gospel'),
        ('Sr', 'Service'),
        ('GA', 'Graduate Application'),
        ('Fs', 'Fellowship'),
        ('Ot', 'Other'),
    )

    # what state this request is in with respect to the TA's approval.
    status = models.CharField(choices=TYPE_APPROVAL_STATUS_CHOICES,
                                  max_length=2, default='Pn')

    # A reason is a category for the motivation behind the request.
    reason = models.CharField(choices=TYPE_REASON_CHOICES,
                                  max_length=2)

    # How many minutes will the web access request be good for once it has been
    # started
    minutes = models.PositiveSmallIntegerField()

    # the date of the request was made.
    date_assigned = models.DateTimeField(auto_now_add=True)
    
    # the date of the request was started.
    time_started = models.DateTimeField(auto_now_add=False)
    
    # for a guest web access request this is used to identify the request.
    # for non guests this field is set when the web access request is started.
    hw_address = MACAddressField(blank=True)

    # for non guests this field is who placed the request.
    trainee = models.ForeignKey(Trainee)

    # field for comments submitted with the request.
    comments = models.TextField(blank=True)

    # field for comments submitted by the TA.
    ta_comments = models.TextField(blank=True)

    #sort by trainee name
    class Meta:
        ordering = ["trainee__account__firstname","hw_address"]

    def __unicode__(self):
        return "[{reason}] {name}. Duration: \
            {duration}".format(
            name=self.trainee.account.get_full_name(),
            reason=self.reason,
            duration=self.minutes)
