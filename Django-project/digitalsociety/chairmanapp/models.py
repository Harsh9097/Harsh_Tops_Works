from django.db import models
from django.utils import timezone
import math


# Create your models here.



class User(models.Model):
    email = models.EmailField(unique=True, max_length=30, blank=False)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_verify = models.BooleanField(default=False)
    otp = models.IntegerField(default=456)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.email


class Chairman(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=20)
    pic = models.FileField(upload_to="media/upload",default="media/default.pic.png")

    def __str__(self):
        return self.firstname


class Societymember(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    contact_no = models.CharField(max_length=20)
    occupation = models.CharField(max_length=30,blank=True,null=True)
    block_no = models.CharField(max_length=10)
    no_of_familymembers = models.CharField(max_length=20,blank=True,null=True)
    dob = models.DateField(max_length=20,blank=True,null=True)
    vehicle_details = models.CharField(max_length=10,blank=True,null=True)
    blood_group = models.CharField(max_length=10,blank=True,null=True)
    house_ownership = models.CharField(max_length=20,blank=True,null=True)
    # city = models.CharField(max_length=20,blank=True,null=True)
    pic = models.FileField(upload_to="media/upload",default="media/default.png")

    def __str__(self):
        return self.firstname

class Notice(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(notice_id = self.id).count()
        print("=======> ncount",ncount)
        return ncount
    
    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago" 
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"




class NoticeViewDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    notice_id = models.ForeignKey(Notice, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = NoticeViewDetails.objects.filter(user_id = self.user_id,notice_id = self.notice_id).count()
        print("=======> ncount",ncount)
        return ncount



    
class Event(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = EventViewDetails.objects.filter(event_id = self.id).count()
        print("=======> ncount",ncount)
        return ncount
    
    
    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago" 
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"


class EventViewDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ncount = EventViewDetails.objects.filter(user_id = self.user_id,event_id = self.event_id).count()
        print("=======> ncount",ncount)
        return ncount


class Complaint(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ccount = ComplaintViewDetails.objects.filter(complaint_id = self.id).count()
        print("=======> ccount",ccount)
        return ccount
    
    def whenpublished(self):
        now = timezone.now()

        diff = now - self.created_at

        if diff.days == 0 and diff.seconds >= 0 and diff.seconds < 60:
            seconds = diff.seconds

            if seconds == 1:
                return str(seconds) + "second ago" 
            else:
                return str(seconds) + "seconds ago"

        if diff.days == 0 and diff.seconds >= 60 and diff.seconds < 3600:
            minutes = math.floor(diff.seconds/60)

            if minutes == 1:
                return str(minutes) + "minute ago"
            else:
                return str(minutes) + "minutes ago"

        if diff.days == 0 and diff.seconds >= 3600 and diff.seconds < 86400:
            hours = math.floor(diff.seconds/3600)

            if hours == 1:
                return str(hours) + "hour ago"
            else:
                return str(hours) + "hours ago"

        if diff.days >= 1 and diff.days < 30:
            days = diff.days

            if days == 1:
                return str(days) + "day ago"
            else:
                return str(days) + "days ago"

        if diff.days >= 30 and diff.days < 365:
            months = math.floor(diff.days/30)

            if months == 1:
                return str(months) + "month ago"
            else:
                return str(months) + "months ago"

        if diff.days >= 365:
            years = math.floor(diff.days/365)

            if years == 1:
                return str(years) + "year ago"
            else:
                return str(years) + "years ago"




class ComplaintViewDetails(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    complaint_id = models.ForeignKey(Complaint, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def count_view(self):
        ccount = ComplaintViewDetails.objects.filter(user_id = self.user_id,notice_id = self.complaint_id).count()
        print("=======> ncount",ccount)
        return ccount



class Maintainance(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    member_id = models.ForeignKey(Societymember , on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    duedate = models.DateField(max_length=30) 
    status = models.CharField(max_length=30,default="PANDING")   
    
