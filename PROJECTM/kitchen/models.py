# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=6, unique=True)
	code = models.CharField(max_length=3)
	active = models.BooleanField()
	category = models.CharField(max_length=9)

	def __str__(self):
		return self.name