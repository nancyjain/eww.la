from django.db import models

# Create your models here.
class EulaInput(models.Model):
    license_text = models.TextField()
    creation_date = models.DateTimeField('date published', auto_now_add=True)
    last_update_datetime = models.DateTimeField('date/time of last edit', auto_now=True)

