from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser

class Turlar(models.Model):
    nomi = models.CharField(max_length=255)

    def __str__(self):
        return self.nomi

class Qurilmalar(models.Model):
    tur = models.ForeignKey(Turlar, on_delete=models.CASCADE)
    nomi = models.CharField(max_length=255)
    tasnif = models.CharField(max_length=255)
    rasmi = models.ImageField(default='static/img/default.jpg')
    holati = models.CharField(max_length=255)
    narxi =  models.DecimalField(max_digits=10, decimal_places=2 ,default=0)


    def __str__(self):
        return self.nomi

class CustomUser(AbstractUser):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    lavozimi = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)  
    password = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.username

class Mijozlar(models.Model):
    ism = models.CharField(max_length=255)
    familiya = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    telefon = models.CharField(max_length=20)
    jinsi = models.CharField(max_length=10)
    pasport = models.CharField(max_length=15)
    jshshir = models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Prokat(models.Model):
    mijoz = models.ForeignKey(Mijozlar, on_delete=models.CASCADE)
    qurilma = models.ForeignKey(Qurilmalar, on_delete=models.CASCADE)
    ishchi = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    berilgan_sanasi = models.DateField(default=timezone.now)
    qaytish_sanasi = models.DateField()
    kunlar_soni = models.BigIntegerField()
    umumiy_narx = models.DecimalField(max_digits=10, decimal_places=2)
    montaj = models.BooleanField(default=False)
    xizmat_narxi = models.DecimalField(max_digits=10, decimal_places=2)
    avans = models.DecimalField(max_digits=10, decimal_places=2)
    miqdori = models.IntegerField()
    kunlik_narxi =  models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return str(self.qurilma)

class Qaytarish(models.Model):
    qaytarilgan_sana = models.DateField(default=timezone.now)
    miqdori = models.IntegerField()
    nosozlik = models.CharField(max_length=255)
    summa = models.BigIntegerField()
    prokat = models.ForeignKey(Prokat, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Tamirlash(models.Model):
    sana = models.DateField(default=timezone.now)
    qurilma = models.ForeignKey(Qurilmalar, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
