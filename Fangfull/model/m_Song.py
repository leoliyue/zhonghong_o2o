
# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Fangfull.model.m_Album import Album

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    class Meta:
        db_table = 'song'
    def __str__(self):
        return self.song_title