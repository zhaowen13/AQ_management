# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class case(models.Model):
    name = models.CharField('用例名称',max_length=100)
    module = models.CharField('所属模块',max_length=100)
    step = models.CharField('操作步骤',max_length=1000)
    result = models.CharField('预期结果',max_length=1000)
    grade = models.CharField('用例等级',max_length=100)
    execution = models.CharField('执行状态',max_length=100)
    cover = models.CharField('覆盖状态',max_length=100)
    def __unicode__(self):
        return self.fundcode
    class Meta:
        db_table = "case"

