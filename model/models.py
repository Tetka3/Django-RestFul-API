from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='model/files/cover')

    def __str__(self):
        return self.name + ' ' + self.description 