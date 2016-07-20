from __future__ import unicode_literals
from ..dloginApp.models import User

from django.db import models

class Courses(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
	user_id = models.ManyToManyField(User)


class Post(models.Model):
	title = models.CharField(max_length=45)
	message = models.TextField(max_length=1000)
	# Notice the association made with ForeignKey for a one-to-many relationship
	user_id = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

