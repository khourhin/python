from django.db import models
from django.utils import timezone

# TODO Here is a really simplified form compared the the present TRUFA setup

class Job(models.Model):
    user = models.ForeignKey('auth.User')
    date = models.DateTimeField(default=timezone.now)
    fake_infile = models.CharField(max_length=100, default='NO_INPUT')
    prog1 = models.BooleanField(default=False)
    prog2 = models.BooleanField(default=False)

    def __str__(self):
        return 'Job by %s, submitted %s' % (self.user, self.date)
