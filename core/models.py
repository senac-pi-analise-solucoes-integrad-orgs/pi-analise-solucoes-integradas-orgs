from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as __


class User(AbstractUser):
    email = models.EmailField(unique=True)

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'


class Address(models.Model):
    zip_code = models.CharField(__('Zip code'), max_length=9)
    state = models.CharField(__('State'), max_length=255)
    city = models.CharField(__('City'), max_length=255)
    neighborhood = models.CharField(__('Neighborhood'), max_length=30)
    street = models.CharField(__('Street'), max_length=255)
    number = models.CharField(__('Number'), max_length=10)
    complement = models.CharField(
        __('Complement'),
        max_length=30,
        blank=True,
        null=True,
    )
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name = __('Address')
        verbose_name_plural = __('Addresses')

    def __str__(self) -> str:
        return (
            f'{self.street.strip()}, '
            f'{self.number.strip()} '
            f'{self.complement.strip()} - ' if self.complement else ''
            f'{self.neighborhood.strip()}, '
            f'{self.city.strip()} - '
            f'{self.state.strip()}, '
            f'{self.zip_code.strip()}'
        )


class PhoneNumber(models.Model):
    phone_number = models.CharField(__('Phone number'), max_length=30)
    whatsapp_number = models.CharField(
        __('WhatsApp phone number'),
        max_length=30,
        blank=True,
        null=True,
    )
    specialist = models.ForeignKey(
        'core.Specialist',
        verbose_name=__('Specialist'),
        on_delete=models.CASCADE,
        related_name='phone_numbers',
        blank=True,
        null=True,
    )
    profile = models.ForeignKey(
        'core.Profile',
        verbose_name=__('Profile'),
        on_delete=models.CASCADE,
        related_name='phone_numbers',
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.phone_number


class Specialty(models.Model):
    name = models.CharField(__('Name'), max_length=255)

    def __str__(self) -> str:
        return self.name


class Specialist(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=__('User'),
        on_delete=models.CASCADE,
        related_name='specialist',
    )
    address = models.ForeignKey(
        'core.Address',
        verbose_name=__('Address'),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='specialists',
    )
    opening_hours = models.CharField(__('Opening hours'), max_length=255)
    specialties = models.ManyToManyField(
        'core.Specialty',
        related_name='specialists',
        blank=True,
    )

    def __str__(self) -> str:
        return self.user.name


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        verbose_name=__('User'),
        on_delete=models.CASCADE,
        related_name='profile',
    )
    date_of_birth = models.DateField(
        verbose_name=__('Date of birth'),
    )

    def __str__(self) -> str:
        return self.user.name


class Review(models.Model):
    rating = models.PositiveSmallIntegerField()
    description = models.CharField(
        __('Description'),
        max_length=255,
        blank=True,
        null=True,
    )
    specialist = models.ForeignKey(
        'core.Specialist',
        verbose_name=__('Specialist'),
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True,
        null=True,
    )
    profile = models.ForeignKey(
        'core.Profile',
        verbose_name=__('Profile'),
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.rating} on {self.created_at.date}'
