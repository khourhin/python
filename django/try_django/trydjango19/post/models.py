from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    # Can be used with instance.user for example
    # to create a folder of upload per users

    # The change can be notice in the nedia root:
    # /media_cdn/19 i.e post.id 19
    return "%s/%s" % (instance.id, filename)


class Post(models.Model):
    title = models.CharField(max_length=120)
    # Image can be served with a models.FileField
    # image = models.FileField(null=True, blank=True)
    # BUT
    #    image = models.ImageField(null=True, blank=True,
    #                             height_field="height_field",
    #                             width_field="width_field")
    # And now with a better upload function

    image = models.ImageField(null=True, blank=True,
                              upload_to=upload_location,
                              height_field="height_field",
                              width_field="width_field")

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    # Don't get now how those timestamps are working ...
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    # BEST DJANGO PRACTICE !!
    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-timestamp', '-updated']
