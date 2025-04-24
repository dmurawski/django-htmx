from django.contrib import admin

from contacts.models import Contact, User

# Register your models here.
admin.site.register(User)
admin.site.register(Contact)
