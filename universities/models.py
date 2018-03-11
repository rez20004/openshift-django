from django.db import models

class Universities(models.Model):
    name = models.CharField(max_length=500)
    iRank = models.IntegerField()
    wRank = models.IntegerField()
    description = models.TextField()
    website = models.CharField(max_length=500)
    acronym = models.CharField(max_length=50)
    founded = models.CharField(max_length=4)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'universities'
