from django.db import models

class TodoList(models.Model):
	title = models.CharField(max_length=250)
	complete = models.BooleanField(default=False, blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title