from django.db import models

""" LOCALITIES models.py

The Localities module is a utility module underlying other apps. In particular,
both trainees are related to localities (as being sent from), and teams are
related to localities (as serving in).

Data Models:
    - Locality: a local church

"""


class Locality(models.Model):
    STATES = (
        ('AL', 'Alabama'),
        ('AK', 'Alaska'),
        ('AZ', 'Arizona'),
        ('AR', 'Arkansas'),
        ('CA', 'California'),
        ('CO', 'Colorado'),
        ('CT', 'Connecticut'),
        ('DE', 'Delaware'),
        ('DC', 'District of Columbia'),
        ('FL', 'Florida'),
        ('GA', 'Georgia'),
        ('HI', 'Hawaii'),
        ('ID', 'Idaho'),
        ('IL', 'Illinois'),
        ('IN', 'Indiana'),
        ('IA', 'Iowa'),
        ('KS', 'Kansas'),
        ('KY', 'Kentucky'),
        ('LA', 'Louisiana'),
        ('ME', 'Maine'),
        ('MD', 'Maryland'),
        ('MA', 'Massachusetts'),
        ('MI', 'Michigan'),
        ('MN', 'Minnesota'),
        ('MS', 'Mississippi'),
        ('MO', 'Missouri'),
        ('MT', 'Montana'),
        ('NE', 'Nebraska'),
        ('NV', 'Nevada'),
        ('NH', 'New Hampshire'),
        ('NJ', 'New Jersey'),
        ('NM', 'New Mexico'),
        ('NY', 'New York'),
        ('NC', 'North Carolina'),
        ('ND', 'North Dakota'),
        ('OH', 'Ohio'),
        ('OK', 'Oklahoma'),
        ('OR', 'Oregon'),
        ('PA', 'Pennsylvania'),
        ('RI', 'Rhode Island'),
        ('SC', 'South Carolina'),
        ('SD', 'South Dakota'),
        ('TN', 'Tennessee'),
        ('TX', 'Texas'),
        ('UT', 'Utah'),
        ('VT', 'Vermont'),
        ('VA', 'Virginia'),
        ('WA', 'Washington'),
        ('WV', 'West Virginia'),
        ('WI', 'Wisconsin'),
        ('WY', 'Wyoming'),
    )

    COUNTRIES = (
        ('USA', 'United States'),
        ('NZ', 'New Zealand'),
        ('AUS', 'Australia'),
        ('CAN', 'Canada'),
        ('CHN', 'China'),
    )

    city = models.CharField(max_length=50)

    # optional for non US localities
    state = models.CharField(max_length=2, blank=True, choices=STATES)

    # for non US localities
    province = models.CharField(max_length=30, blank=True)

    country = models.CharField(max_length=5, choices=COUNTRIES, default='USA')

    def __unicode__(self):
        if self.state:
            return self.city + ', ' + self.state
        else:
            return self.city + ', ' + self.country

    class Meta:
        verbose_name_plural = 'localities'
