from django.db import models

from terms.models import Term

class Badge(models.model):
    """
    A training badge. There are different badges for trainees,
    staff and so forth. Otherwise known as a profile picture.
    """

    BADGE_TYPES = (
        ('T', 'Trainee'),
        ('S', 'Staff'),
    )



    type = models.CharField(max_length=2, choices=BADGE_TYPES)
    original = models.ImageField(upload_to='badges/'+self.construct_upload_path)


    def construct_upload_path(self):
        path = ""
        if self.type = 'T':
            return path + "trainees/" + Term.current_term().code + '/'
        elif self.type = 'S':
            return path + "staff/"