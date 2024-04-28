from django.db import models

# Create your models here.



class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=100)

class worker(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    experience = models.CharField(max_length=150)
    age = models.CharField(max_length=5)
    IDproof = models.CharField(max_length=15)
    lattitude = models.CharField(max_length=20)
    longitude = models.CharField(max_length=20)
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)

class user(models.Model):
    LOGIN = models.ForeignKey(login,default=1,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    place = models.CharField(max_length=100)
    post = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

class category(models.Model):
    name = models.CharField(max_length=100)

class service(models.Model):
    service = models.CharField(max_length=100)
    amount = models.IntegerField()
    CATEGORY=models.ForeignKey(category,on_delete=models.CASCADE,default=1)
    WORKER = models.ForeignKey(worker,on_delete=models.CASCADE,default=1)

class Bookings(models.Model):
    date = models.CharField(max_length=100)
    amount = models.IntegerField()
    lattitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    workerstatus = models.CharField(max_length=20)
    USER = models.ForeignKey(user,on_delete=models.CASCADE,default=1)
    SERVICE = models.ForeignKey(service,on_delete=models.CASCADE,default=1)

class Bill(models.Model):
    amount = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    item = models.CharField(max_length=100)
    BOOKING = models.ForeignKey(Bookings,on_delete=models.CASCADE,default=1)

class chat(models.Model):
    WORKER =models.ForeignKey(worker,default=1,on_delete=models.CASCADE)
    USER =models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    date =models.CharField(max_length=15)
    chat =models.CharField(max_length=20)
    type =models.CharField(max_length=50)

class feedback(models.Model):
    USER =models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    feedback =models.CharField(max_length=25)
    date =models.CharField(max_length=15)

class rating(models.Model):
    BOOKINGS =models.ForeignKey(Bookings,default=1,on_delete=models.CASCADE)
    USER =models.ForeignKey(user,default=1,on_delete=models.CASCADE)
    rating =models.CharField(max_length=15)
    date =models.CharField(max_length=15)

class work(models.Model):
    WORKER =models.ForeignKey(worker,default=1,on_delete=models.CASCADE)
    work_image =models.CharField(max_length=200)
    details =models.CharField(max_length=100)
    date =models.CharField(max_length=15)

class Complaint(models.Model):
    complaint = models.CharField(max_length=100)
    complaint_date = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE, default=1)


