from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone

class OpenSecretUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_pic = models.ImageField(default="media/default.jpg", blank=True, upload_to='media')
    friends = models.ManyToManyField('self', blank=True, related_name='friends')
    messages = models.ManyToManyField('message', blank=True, related_name='messages')
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.user.username

class Message(models.Model):
    msg = models.CharField(max_length=128)
    d_t = models.DateTimeField(default=timezone.now, blank=True)
    sender = models.ForeignKey(OpenSecretUser,on_delete=models.CASCADE,related_name='sender',null=True)
    receiver = models.ForeignKey(OpenSecretUser,on_delete=models.CASCADE,related_name='receiver',null=True)

    def __str__(self):
        return str(self.sender.id) + " " + str(self.receiver.id) + " " + self.msg