from django.contrib.auth.models import AbstractUser, Permission, Group
from django.db import models


class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)  # Additional field for user bio
    # Override the groups field to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Set a custom related name
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    # Override the user_permissions field to avoid conflicts
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_set',  # Set a custom related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username  # Or return any other representation you prefer
