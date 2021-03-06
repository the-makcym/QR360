from django.contrib.auth.base_user import BaseUserManager


class QRUserManager(BaseUserManager):

    def create_user(self, username, password=None, email=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')

        qruser = self.model(username=username, **extra_fields)
        qruser.set_password(password)
        qruser.save()

        return qruser

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)
