# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Res_data(models.Model):
    data_id = models.AutoField(primary_key=True,db_column = 'data_id')
    data_name = models.CharField(max_length=250)
    data_stuts = models.SmallIntegerField(default=1)
    data_describe = models.CharField(max_length=1000)
    class Meta:
        db_table = 'res_data'
    def __str__(self):
        return self.data_id
