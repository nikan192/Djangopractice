from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Games(models.Model) :

    users = models.ForeignKey(User , default = None , on_delete = models.CASCADE)

    image = models.ImageField(upload_to = 'gamecovers/' , blank = True , null = True)

    name = models.CharField(max_length = 24)
    
    description = models.TextField()

    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add = True)

    updated_at = models.DateTimeField(auto_now = True)

    #deleted_at = models.DateTimeField(null = True , blank= True)

    class Meta :
        ordering = ('name',)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("Gamepage", kwargs={"pk" : self.id})
    
    pass


class Special_Games(models.Model) :

    image = models.ImageField(upload_to='gamecovers/' , blank = True , null = True)

    name = models.CharField(max_length=24)
    
    description = models.TextField()

    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse("Gamepage", kwargs={"pk" : self.id})

    pass