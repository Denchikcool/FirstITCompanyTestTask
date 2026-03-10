from django.db import models
from django.forms import ValidationError

class Status(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    created_at = models.DateField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True)

    def __str__(self):
        return f"{self.amount} - {self.category}"
    
    def clean(self):
        if self.subcategory.category != self.category:
            raise ValidationError("Подкатегория не принадлежит категории")

        if self.category.type != self.type:
            raise ValidationError("Категория не принадлежит типу")