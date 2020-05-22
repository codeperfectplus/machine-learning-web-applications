from django.db import models

# Create your models here.

class IrisModel(models.Model):
    sepal_length = models.DecimalField(decimal_places=2,max_digits=5)
    sepal_width = models.DecimalField(decimal_places=2,max_digits=5)
    petal_length = models.DecimalField(decimal_places=2,max_digits=5)
    petal_width = models.DecimalField(decimal_places=2,max_digits=5)

    def __str__(self):
        return "Flower Length and Width"
    
    