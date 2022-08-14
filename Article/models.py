from django.db import models
from django.contrib.auth import get_user_model



class Post(models.Model):
    STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE , related_name='user')
    title = models.CharField(max_length=100)
    text = models.TextField()
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=3)

    

    def __str__(self):

        return self.title



class Static(models.Model):

    post= models.ForeignKey(Post , on_delete=models.CASCADE , related_name='posts')
    total_trade = models.IntegerField()
    average_loss = models.IntegerField()
    net_profit = models.IntegerField()
    win_rate= models.IntegerField()


    def __int__(self):

        return self.win_rate