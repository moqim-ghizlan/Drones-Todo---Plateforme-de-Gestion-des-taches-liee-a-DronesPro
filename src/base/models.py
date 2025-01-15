from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Todo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, related_name='creator')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='todos', null=True, blank=True)


    class Meta:
        ordering = ('completed', '-created_at')

    def _str_(self):
        return self.title

    def get_title(self):
        return self.title

    def get_display_title(self):
        if self.title:
            if len(self.title) > 40:
                return self.title[:40] + "..."
            else:
                return self.title
        return "No title"

    def get_description(self):
        return self.description if self.description else ""

    def get_display_description(self):
        return self.description if self.description else "No description"

    def get_completed(self):
        return self.completed


    def set_completed(self):
        self.completed_at = datetime.now()
        self.completed = True
        self.save()


    def set_incomplete(self):
        self.completed_at = None
        self.completed = False
        self.save()

    def get_category(self):
        return self.category.name if self.category else "No category"



class Category(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def get_counter(self):
        todos = Todo.objects.filter(category=self)
        return len(todos)


class User(AbstractUser):
    email = models.EmailField(max_length=254, null=False, unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']



@receiver(pre_save, sender=Category)
def store_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)