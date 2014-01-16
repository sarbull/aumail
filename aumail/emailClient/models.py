from django.db import models

# Create your models here.

class email_users(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	def __unicode__(self):
		return self.name


class user_notebook(models.Model):
	notebook_entry = models.ForeignKey(email_users)
	entry_name = models.CharField(max_length=50)
	entry_email = models.CharField(max_length=50)
	def __unicode__(self):
		return self.entry_name