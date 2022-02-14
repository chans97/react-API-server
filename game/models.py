from django.db import models


class GameUser(models.Model):
    name = models.CharField(max_length=6)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.name