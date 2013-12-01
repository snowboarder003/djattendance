from django.db import models

from terms.models import Term
from .util import _image_upload_path


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
    original = models.ImageField(upload_to=_image_upload_path)

    def get_upload_path(self, filename, term=Term.current_term()[0].code):
        path = "badges/"
        if self.type == 'T':
            path += "trainees/" + term + '/'
        elif self.type == 'S':
            path += "staff/"
        return path + filename

    def __unicode__(self):
        return u"[%s] %s" % (self.type, self.original.name)