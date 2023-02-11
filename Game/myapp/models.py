from django.db import models
from django.contrib.auth.models import User

class Song(models.Model):
    User= models.ManyToManyField(User)
    Song_name= models.CharField(max_length=50)
    Song_duration=models.IntegerField()
    def written_by(self):
     return "," .join([str(p) for p in self.User.all()])

