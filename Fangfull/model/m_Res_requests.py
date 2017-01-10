# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Res_requests(models.Model):
    requests_id = models.AutoField(primary_key=True,db_column = 'requests_id')
    requests_addres = models.CharField(max_length=250)
    requests_describe = models.CharField(max_length=1000)
    requests_stuts = models.SmallIntegerField(default=1)
    requests_data = models.CharField(max_length=1000)
    class Meta:
        db_table = 'res_requests'
    def __str__(self):
        return self.requests_id