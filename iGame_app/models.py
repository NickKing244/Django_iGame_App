from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First name must be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last name must be at least 2 characters"
        if len(postData['email']) < 4:
            errors['email'] = "Email is too short"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        if postData['password'] != postData['password_conf']:
            errors['match'] = "Password and password confirmation do not match!"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = "Invalid Email Address"
        users_with_email = User.objects.filter(email=postData['email'])
        if len(users_with_email) >= 1:
            errors['dupe'] = "Email taken, use another"
        return errors
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors['first_name'] = "First name field is required"
        if len(postData['last_name']) < 1:
            errors['last_name'] = "Last name field is required"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['regex'] = "Invalid Email Address"
        if len(postData['email']) < 4:
            errors['email'] = "Email is too short"
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters"
        return errors

class GameManager(models.Manager):
    def game_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors['title'] = "Title must be at least 2 characters"
        if len(postData['developer']) < 2:
            errors['developer'] = "Developer must be at least 2 characters"
        if len(postData['publisher']) < 2:
            errors['publisher'] = "Publisher must be at least 2 characters"
        if len(postData['platform']) < 2:
            errors['platform'] = "Platform must be at least 2 characters"
        if len(postData['genre']) < 2:
            errors['genre'] = "Genre must be at least 2 characters"
        if len(postData['summary']) < 2:
            errors['summary'] = "Summary must be at least 2 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Game(models.Model):
    title = models.CharField(max_length=255)
    developer = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
    summary = models.TextField()
    release_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = GameManager()