from django.contrib import admin

from products.admin import BasketAdmin
from users.models import EmailVerification, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_staff', 'email']
    # fields = ['name', 'category', ('price', 'quantity'), 'description', 'image', 'slug']
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'expiration')
    fields = ('user', 'created', 'expiration', 'code')
    readonly_fields = ('created', )
