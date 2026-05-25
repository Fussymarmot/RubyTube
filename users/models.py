from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
        db_table = 'users'

    def __str__(self):
        return self.username
