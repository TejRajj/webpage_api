from django.db import models

# Create your models here.
class LoginDB(models.Model):
    Full_name = models.CharField(max_length=20)
    Country = models.CharField(max_length=10)
    Manual_id = models.IntegerField()

    def __str__(self):
        return self.Full_name