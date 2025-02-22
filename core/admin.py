from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as __

from core.models import (
    Address,
    PhoneNumber,
    Specialty,
    Specialist,
    Review, User, Profile,
)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'zip_code',
        'state',
        'city',
        'neighborhood',
        'street',
        'number',
    )
    search_fields = (
        'zip_code',
        'state',
        'city',
        'neighborhood',
        'street',
    )


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'phone_number',
        'whatsapp_number',
    )
    search_fields = (
        'phone_number',
    )


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'name',
    )
    search_fields = (
        'name',
    )


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'user__first_name',
        'user__last_name',
        'address',
        'opening_hours',
        '_specialties',
    )
    search_fields = (
        'user__first_name',
        'user__last_name',
        'address',
        'opening_hours',
        'specialties',
    )

    @staticmethod
    @admin.display(description=__('Specialties'))
    def _specialties(obj: Specialist):
        if obj.specialties:
            specialties = [
                speciality.name for speciality in obj.specialties.all()
            ]
            return ', '.join(specialties)
        return None


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'user__first_name',
        'user__last_name',
        'date_of_birth',
    )
    search_fields = (
        'user__first_name',
        'user__last_name',
    )

    @staticmethod
    @admin.display(description=__('Specialties'))
    def _specialties(obj: Specialist):
        if obj.specialties:
            specialties = [
                speciality.name for speciality in obj.specialties.all()
            ]
            return ', '.join(specialties)
        return None


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    # List
    list_display = (
        'rating',
        'specialist',
        'profile',
    )
    search_fields = (
        'specialist',
        'profile',
    )
