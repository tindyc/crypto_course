from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Create Contact form section in Admin Panel"""

    readonly_fields = (
        'subject',
        'first_name',
        'last_name',
        'email',
        'phone_number',
        'your_message',
        'date_sent',
    )

    list_display = (
        'subject',
        'first_name',
        'email',
        'date_sent',
    )

    ordering = ('-date_sent',)


admin.site.register(Contact, ContactAdmin)
