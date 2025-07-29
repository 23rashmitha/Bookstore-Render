from django.db import models

class TeluguBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class HindiBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class EnglishBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class FrenchBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class KannadaBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title


class MechanicalBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class CivilBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class CseBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class EceBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class EeeBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class ChemicalBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover_image = models.URLField(blank=True)
    rating = models.FloatField(default=0.0)
    stock_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
