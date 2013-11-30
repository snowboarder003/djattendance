from django.db import models

from terms.models import Term
from .util import construct_upload_path

class Badge(models.Model):
    """
    A training badge. There are different badges for trainees,
    staff and so forth. Otherwise known as a profile picture.
    """

    BADGE_TYPES = (
        ('T', 'Trainee'),
        ('S', 'Staff'),
    )

    type = models.CharField(max_length=2, choices=BADGE_TYPES)
    original = models.ImageField(upload_to='badges/'+construct_upload_path(type))
