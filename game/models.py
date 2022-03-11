from django.db import models


class GameUser(models.Model):
    title = models.CharField(max_length=20, null=True)
    contents = models.CharField(default="", null=True, max_length=1000)

    def __str__(self):
        return self.title

class Repl(models.Model):
    contents = models.CharField(default="", null=True, max_length=1000)
    post = models.ForeignKey("GameUser",  on_delete=models.CASCADE, null=True, blank=True, related_name='repls')

    def __str__(self):
        return self.contents