from django.db import models
from authentication.models import baseModel, membersModel
from authentication.helpers import custom_file_name
from main.utils.constant import PERMISSIONS

from datetime import datetime


class services(baseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(services, self).save(*args, **kwargs)

class clubBooking(baseModel):
    member_id = models.ForeignKey(membersModel, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=255, blank=False)
    from_date = models.DateField()
    to_date = models.DateField()
    content = models.TextField()
    total_days = models.IntegerField(blank=True)
    status = models.CharField(default='Pending', max_length=50, choices=PERMISSIONS)

    def __str__(self):
        return f"{self.member_id} - {self.event_name}"
    
    def save(self, *args, **kwargs):
        fdate = str(self.from_date)
        tdate = str(self.to_date)

        def string_to_date(date_string):
            try:
                date_object = datetime.strptime(date_string, '%Y-%m-%d').date()
                return date_object
            except ValueError:
                # Handle invalid date strings here
                return None
            
        def date_difference_in_days(self):
            if fdate and tdate:
                difference = string_to_date(tdate) - string_to_date(fdate)
                return difference.days + 1
            else:
                return None
        self.total_days = date_difference_in_days(self)
        print(type(self.total_days))
        super(clubBooking, self).save(*args, **kwargs)

class catagory(baseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        super(catagory, self).save(*args, **kwargs)

class Events(baseModel):
    DIR_NAME = 'Event'
    image = models.FileField(upload_to=custom_file_name, default='default-event.png')
    catagory = models.ForeignKey(catagory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.catagory} - {self.title}"
    
class Gallery(baseModel):
    DIR_NAME = 'member_profiles'
    photo = models.FileField(upload_to=custom_file_name, default='default-profile.png')
    file_date = models.DateField(default=datetime.now)

class emergency_contacts(baseModel):
    DIR_NAME = 'Emergency contact'
    emergency_photo = models.FileField(upload_to=custom_file_name, default='default-event.png')
    contact_name = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.contact_name}"
