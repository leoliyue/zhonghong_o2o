# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Message_res(models.Model):
    res_id = models.AutoField(primary_key=True,db_column = 'res_id')
    res_name = models.CharField(max_length=250)
    res_describe = models.CharField(max_length=1000)
    class Meta:
        db_table = 'message_res'
    def __repr__(self):
        return self.res_id + " - " + self.res_name
