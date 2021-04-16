from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Goods(models.Model):
    g_name = models.CharField(max_length=128)
    g_price = models.IntegerField()


class productionDate(models.Model):
    production_date = models.CharField(max_length=128)
    good = models.ForeignKey('shop.Goods', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, )
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'customer'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Customer.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.customer.save()


class Order(models.Model):
    customer = models.ForeignKey('shop.Customer', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer},{self.created_date}'
