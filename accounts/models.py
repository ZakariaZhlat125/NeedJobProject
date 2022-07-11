from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField

# custom manager


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


GENDER_CHOICES = (
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Other"),
)


class User(AbstractUser):
    username = None
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    date_of_birth = models.DateField(default='1990-01-01')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    picture = models.ImageField(
        upload_to='img/users', null=True, verbose_name=""
    )
    phone = PhoneNumberField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    objects = UserManager()
    """
    def save(self, **kwargs):
        if not (self.is_staff or self.is_superuser):
            password = self.password
            if password is not None:
                self.set_password(password)
            super(User, self).save(**kwargs)
            name = f"{self.first_name} {self.last_name}"
            Profile.objects.create(
                name=name, dob=self.date_of_birth, user=self)
            return self
        else:
            return super(User, self).save(**kwargs)
    """
    def __str__(self):
        return self.email