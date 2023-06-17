from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Games(models.Model) :

    image = models.ImageField(upload_to='gamecovers/' , blank = True , null = True)

    name = models.CharField(max_length=24)
    
    description = models.TextField()

    price = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    #deleted_at = models.DateTimeField(null = True , blank= True)

    def __str__(self) -> str:
        return self.name

    def delete(self , using = None , keep_parent = False) :
        self.deleted_at = timezone.now()
        self.save()
        pass

    def restore(self) :
        self.deleted_at = None
        self.save()
        pass

    def is_deleted(self) :
        self.deleted_at = None
        self.save()
        pass

    def get_absolute_url(self):
        return reverse("Gamepage", kwargs={"pk": self.id})

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

    def delete(self , using = None , keep_parent = False) :
        self.deleted_at = timezone.now()
        self.save()
        pass

    def restore(self) :
        self.deleted_at = None
        self.save()
        pass

    def is_deleted(self) :
        self.deleted_at = None
        self.save()
        pass

    def get_absolute_url(self):
        return reverse("Gamepage", kwargs={"pk": self.id})

    pass