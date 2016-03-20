from django.db import models

# Create your models here.

class What(models.Model):
    what_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.what_name


class Who(models.Model):
    who_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.who_name


class Type1(models.Model):
    type_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.type_name


class Where(models.Model):
    where_name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.where_name


class List(models.Model):
    pub_date_time = models.DateTimeField('date published')
    pub_date = models.DateTimeField('date')
    type_name = models.ManyToManyField(Type1, null=True, related_name='type', blank=True )
    what_name = models.ManyToManyField(What, null=True, related_name='what', blank=True)
    who_name = models.ManyToManyField(Who, null=True, related_name='who', blank=True)
    where_name = models.ManyToManyField(Where, null=True, related_name='where', blank=True)
    def __unicode__(self):
        return self.what_name