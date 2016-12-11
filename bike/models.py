from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# from eventlog.models import log

# Create your models here.
# class SignUp(models.Model):
# 	email = models.EmailField()
# 	full_name = models.CharField(max_length=100,blank=False,null=True,default='')
# 	timestamp = models.DateTimeField(auto_now_add=True,auto_now=False)
# 	updated = models.DateTimeField(auto_now_add=False,auto_now=True)

# 	def __str__(self): # for python 2 use unicode instead of str
# 		return self.email

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        # Uncomment if you don't want the slug to change every time the name changes
        #if self.id is None:
                #self.slug = slugify(self.name)
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    def __unicode__(self):
        return self.user.username