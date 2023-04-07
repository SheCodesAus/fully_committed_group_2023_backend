from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):

    def __str__(self):
        return self.username
    
    def set_password_with_validation(self, old_password, new_password):
        if self.check_password(old_password):
            self.set_password(new_password)
            self.save()
            return True
        else:
            return False