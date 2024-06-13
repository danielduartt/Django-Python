from django.db import models

class Autor(models.Model):
    name = models.CharField(max_length = 100)
    birth_date = models.DateField()
    def __str__(self): 
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 100)
    author = models.ForeignKey(Autor, on_delete = models.CASCADE, related_name = 'book')
    published_date = models.DateField()
    def __str__(self): 
        return self.title
    