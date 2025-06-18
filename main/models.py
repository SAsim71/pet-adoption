from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to='pets/')
    description = models.TextField()
    adopted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PetImage(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='pets/extra/')

    def __str__(self):
        return f"Extra image for {self.pet.name}"

class Adoption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    adopter_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.adopter_name} adopted {self.pet.name}"
