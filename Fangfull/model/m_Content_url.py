# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Content_url(models.Model):
    url_id = models.AutoField(primary_key=True,db_column = 'url_id')
    url_blue = models.CharField(max_length=250)
    url_red = models.CharField(max_length=250)
    url_type =models.CharField(max_length=250)
    url_stuts = models.SmallIntegerField(default=1)
    sql_id = models.CharField(max_length=250)

    class Meta:
        db_table = 'content_url'
    # def get_absolute_url(self):
        # return reverse('fangfull:viewContenturl',kwargs={'pk':self.pk})
    def __str__(self):
        return self.url_id

