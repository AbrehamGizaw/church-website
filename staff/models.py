from django.db import models


class Believer(models.Model):
    full_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='believers', blank=True, null=True)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    address = models.TextField()
    joined_date = models.DateField()
    CATEGORY_CHOICES = [
        ('child', 'Child'),
        ('teenager', 'Teenager'),
        ('adult', 'Adult'),
        ('elders', 'Elders'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    SERVICE_GROUP_CHOICES = [
        ('none', 'None'),
        ('prophet', 'Prophet'),
        ('apostle', 'Apostle'),
        ('pastor', 'Pastor'),
        ('evangelical', 'Evangelical'),
        ('deacons', 'Deacons'),
        ('singer', 'Singer'),
        ('elder', 'Elder'),
    ]
    service_group = models.CharField(max_length=100, choices=SERVICE_GROUP_CHOICES)
    STATUS_CHOICES = [
        ('pastor', 'Pastor'),
        ('untaken', 'Untaken'),
    ]
    status = models.CharField(max_length=100, choices=STATUS_CHOICES)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
class Education(models.Model):
    program = models.CharField(max_length=100)
    lecturer = models.CharField(max_length=100)
    section = models.CharField(max_length=100)
    started_date = models.DateField()
    end_date = models.DateField()
    documents = models.FileField(upload_to='education_documents')
    messages = models.TextField()
    learners = models.ManyToManyField('Believer')

class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='events')
    start_date = models.DateField()
    end_date = models.DateField()

class Expense(models.Model):
    reason = models.CharField(max_length=255)
    taker = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    date = models.DateField()

class Fellowship(models.Model):
    pastor = models.CharField(max_length=100)
    believers = models.ManyToManyField('Believer')
    message = models.TextField()
    image = models.ImageField(upload_to='fellowships', blank=True, null=True)
    documents = models.FileField(upload_to='fellowship_documents', blank=True, null=True)


class GroupChat(models.Model):
    members = models.ManyToManyField('Believer')
    message = models.TextField()
    image = models.ImageField(upload_to='group_chat', blank=True, null=True)
    documents = models.FileField(upload_to='group_chat_documents', blank=True, null=True)
    GROUP_CHOICES = [
        ('prayer', 'Prayer'),
        ('classes', 'classes'),
        ('compassion', 'Compassion'),
        ('quires', 'Quires'),
        ('pastors', 'Pastors'),
        ('deacons', 'Deacons'),
        ('elders', 'Elders'),
        ('teachers', 'Teachers'),
    ]
    group = models.CharField(max_length=100, choices=GROUP_CHOICES)

class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    reason = models.CharField(max_length=255)
    payer = models.CharField(max_length=100)
    date = models.DateField()
    balance = models.DecimalField(max_digits=10, decimal_places=2)


class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='news')
    date = models.DateField()

class Stock(models.Model):
    category = models.CharField(max_length=100)
    mark = models.CharField(max_length=100)
    buyer = models.CharField(max_length=100)
    expense = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    quantity = models.IntegerField()
    name = models.CharField(max_length=100)

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    place = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials')
    contact_phone = models.CharField(max_length=20)
    date_served = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()