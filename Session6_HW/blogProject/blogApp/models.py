from django.db import models

# Create your models here.
choices = (
              ('movie', 'movie'),
              ('drama', 'drama'),
              ('programming', 'programming'),
    )
class Article(models.Model):
    choice = models.CharField(max_length =11, choices= choices, default='drama')
    title = models.CharField(max_length=200, help_text="max 200")
    content = models.TextField()
    
    wrote_time = models.DateTimeField(auto_now_add=True) 
    def __str__(self):
        return self.title

TTL = Article(models.Model)
print(TTL)
     


        
