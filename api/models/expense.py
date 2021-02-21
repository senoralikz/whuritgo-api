from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Expense(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  item = models.CharField(max_length=100)
  quantity = models.IntegerField()
  date = models.CharField(max_length=100)
  cost = models.DecimalField(max_digits=None, decimal_places=2)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return self.item

  def as_dict(self):
    """Returns dictionary version of Mango models"""
    return {
        'id': self.id,
        'item': self.item,
        'quantity': self.quantity,
        'date': self.date,
        'cost': self.cost
    }
