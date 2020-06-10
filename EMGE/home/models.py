from django.db import models

# Create your models here.
class MenApparel(models.Model):
    product_image = models.ImageField()
    product_name = models.TextField()
    product_price = models.CharField(max_length=200, null=True)
    product_offer = models.FloatField(null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'menapparels'


class womenApparel(models.Model):
    product_image = models.ImageField()
    product_name = models.TextField()
    product_price = models.CharField(max_length=200, null=True)
    product_offer = models.FloatField(null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'womenapparels'

class KidApparel(models.Model):
    product_image = models.ImageField()
    product_name = models.TextField()
    product_price = models.CharField(max_length=200, null=True)
    product_offer = models.FloatField(null=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name_plural = 'kidapparels'
