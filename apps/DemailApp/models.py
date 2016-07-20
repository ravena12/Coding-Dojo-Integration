from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class EmailManager(models.Manager):

	def validEmail(self, email):
		if not EMAIL_REGEX.match(email):
			return False
		else:
			return True


class Email(models.Model):
	email = models.EmailField()
	created_at = models.DateField(auto_now_add = True)
	updated_at = models.DateField(auto_now_add = True)
	emailManager = EmailManager()