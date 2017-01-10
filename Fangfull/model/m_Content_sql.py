# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
from Fangfull.model.m_Content_url import Content_url

class Content_sql(models.Model):

    sql_id = models.AutoField(primary_key=True,db_column='sql_id')
    sql_name = models.CharField(max_length=200)
    sql_host = models.CharField(max_length=100)
    sql_port = models.CharField(max_length=50)
    sql_user_name = models.CharField(max_length=250)
    sql_user_passwd = models.CharField(max_length=250)
    sql_db = models.CharField(max_length=250)
    sql_stuts = models.SmallIntegerField(default=1)


    class Meta:
        db_table = 'content_sql'
    def __str__(self):
        return self.sql_id


