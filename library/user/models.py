from django.db import models
import datetime

ROLE_CHOICES = (
    (0, "visitor"),
    (1, "librarian"),
)


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=20, default=None)
    surname_name = models.CharField(max_length=20, default=None)
    email = models.EmailField(max_length=50, unique=True, default=None)
    password = models.CharField(max_length=30, default=None)
    created_at = models.DateTimeField(auto_now=datetime.datetime.now(), editable=False)
    last_login = models.DateTimeField(auto_now=datetime.datetime.now())
    role = models.IntegerField(choices=ROLE_CHOICES, default=0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    def __str__(self):
        """
        Magic method is redefined to show all information about CustomUser.
        :return: user id, user first_name, user middle_name, user last_name,
                 user email, user password, user updated_at, user created_at,
                 user role, user is_active
        """
        return f"'id': {self.id}, 'first_name': '{self.first_name}', 'middle_name': '{self.middle_name}', 'last_name': '{self.last_name}', 'email': '{self.email}', 'created_at': {int(self.created_at.timestamp())}, 'updated_at': {int(self.updated_at.timestamp())}, 'role': {self.role}, 'is_active': {self.is_active}"  # 'password': '{self.password}', \
