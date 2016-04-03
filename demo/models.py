from __future__ import unicode_literals

from django.db import models


CHAR_CHOICES = (
    ('CH1', 'Choice 1'),
    ('CH2', 'Choice 2'),
    ('CH3', 'Choice 3'),
    ('CH4', 'Choice 4'),
)


class Demo(models.Model):
    date = models.DateField()
    char = models.CharField(max_length=16, choices=CHAR_CHOICES)
    
    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('demo_list', )