from django.db import models
from django.test import TestCase
from django.conf import settings
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from django.forms import fields as django_fields
from django.contrib.auth.models import User
from nowandthen.models import Picture

#The unit test failed. It was not clear how to correct it, given that the max_length attribute is set to 
#190 in Models. 

class PictureUnitTests(TestCase):
    def test_ensure_title_character_limit_not_exceeded(self):
    #Ensures the character limit for 'title' in Picture is not exceeded. 
        picture = Picture(title='this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. this will exceed 190 characters. ')
        picture.save()
        self.assertEqual((len(picture.title) <= 190), True)


