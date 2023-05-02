from django.db import models


class Projetos(models.Model):
    projeto = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    tir_media = models.CharField(max_length=100)
    total_captado = models.CharField(max_length=100)
    vgv = models.CharField(max_length=100, null=True)


