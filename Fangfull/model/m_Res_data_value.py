# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from Fangfull.model.m_Res_data import Res_data

class Res_data_value(models.Model):

    values_id = models.AutoField(primary_key=True,db_column = 'value_id')
    data = models.ForeignKey(Res_data,on_delete=models.CASCADE)
    value_name = models.CharField(max_length=250)
    value_time = models.DateField(auto_now_add=True)
    value_describe = models.CharField(max_length=1000)
    value_stuts = models.SmallIntegerField(default=1)

    class Meta:
        db_table = 'res_data_value'
    def __str__(self):
        return self.values_id
