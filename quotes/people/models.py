import datetime

from django.db import models
from django.utils import timezone

class Person(models.Model):
    # Person who is quoted
    person_name = models.CharField(max_length=200)
    slug = models.SlugField()
    wiki = models.URLField('Authors Wikipedia Page')

    pub_date = models.DateTimeField('date published',default=datetime.datetime.now())
    updated_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):              # __unicode__ on Python 2
        return self.person_name

class Quote(models.Model):
    person = models.ForeignKey(Person)
    slug = models.SlugField()
    quote_text = models.TextField()
    source = models.TextField()
    topics = models.CharField(max_length=200)
    date = models.CharField(max_length=5)

    pub_date = models.DateTimeField('date published', default=datetime.datetime.now())
    updated_date = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):              # __unicode__ on Python 2
        return self.quote_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
