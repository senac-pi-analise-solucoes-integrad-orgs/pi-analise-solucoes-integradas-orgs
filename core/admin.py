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
        'specialists__user__email',
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
        'whatsapp_number',
        'specialist__user__email',
        'profile__user__email',
    )

    # Details
    autocomplete_fields = (
        'specialist',
        'profile',
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
        'user__email',
        'user__first_name',
        'user__last_name',
        'address',
        'opening_hours',
        'specialties',
    )
    list_filter = (
        'specialties',
    )

    # Details
    autocomplete_fields = (
        'user',
        'specialties',
    )
    raw_id_fields = (
        'address',
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
        'user__email',
        'user__first_name',
        'user__last_name',
    )

    # Details
    autocomplete_fields = (
        'user',
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
        'specialist__user__email',
        'profile__user__email',
    )
    list_filter = (
        'rating',
    )

    # Details
    autocomplete_fields = (
        'specialist',
        'profile',
    )
