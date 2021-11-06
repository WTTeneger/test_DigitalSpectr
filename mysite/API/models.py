from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class UserData(models.Model):
    email = models.EmailField(verbose_name='email')
    phone_number = models.CharField(verbose_name='телефон', max_length=12)
    message = models.TextField(verbose_name='сообщение', blank=True, max_length=5000)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.email
