
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    class Meta:
        db_table = 'album'
    # def get_absolute_url(self):
    #     return reverse('fangfull:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.album_title + ' - ' +self.artist

