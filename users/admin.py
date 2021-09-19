from django.contrib import admin

# Register your models here.
from users.models import OTPCode

admin.site.register(OTPCode)