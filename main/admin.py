from django.contrib import admin
from .models import services, clubBooking, Events, catagory, Gallery
from django.contrib.auth.models import Group, User

admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(services)
admin.site.register(clubBooking)
admin.site.register(Events)
admin.site.register(catagory)
admin.site.register(Gallery)