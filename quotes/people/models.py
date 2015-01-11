import datetime

from django.db import models
from django.utils import timezone

class Person(models.Model):
    # Person who is quoted
    person_name = models.CharField(max_length=200)
    slug = models.SlugField()
    pub_date = models.DateTimeField('date published')
    updated_date = models.DateTimeField(default=datetime.datetime.now())
    wiki = models.URLField('Authors Wikipedia Page')
    def __str__(self):              # __unicode__ on Python 2
        return self.person_name

class Quote(models.Model):
    person = models.ForeignKey(Person)
    slug = models.SlugField()
    quote_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    updated_date = models.DateTimeField(default=datetime.datetime.now())
    topics = models.TextField()
    def __str__(self):              # __unicode__ on Python 2
        return self.quote_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
