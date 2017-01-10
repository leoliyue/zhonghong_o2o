# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Fangfull.model.m_Message_res import Message_res

class Message_data(models.Model):
    data_id = models.IntegerField(primary_key=True)
    data_id = models.AutoField(primary_key=True,db_column = 'data_id')
    data_name = models.CharField(max_length=250)
    data_value = models.CharField(max_length=1000)
    data_describe = models.CharField(max_length=1000)
    res = models.ForeignKey(Message_res,on_delete=models.CASCADE)
    class Meta:
        db_table = 'message_data'
    def __str__(self):
        return self.data_id

