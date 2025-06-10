from django.db import models

class Film(models.Model):
    name = models.CharField(max_length=100)
    iso = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} ISO {self.iso}"

class CekimKosulu(models.Model):
    aydinlatma = models.CharField(max_length=200)
    hava_durumu = models.CharField(max_length=100)

    def __str__(self):
        return self.aydinlatma

class Poz(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    kosul = models.ForeignKey(CekimKosulu, on_delete=models.CASCADE)
    tarih = models.DateField()
    notlar = models.TextField(blank=True)

    def __str__(self):
        return f"{self.film} - {self.tarih}"
