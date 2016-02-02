from django.db import models

class Article(models.Model):
   article = models.TextField()
   post_date = models.DateTimeField('date posted')
   title = models.CharField(max_length=128)
  
def _str_(self):
 return "Blog(title = '%s')"%(self.title)

# Create your models here.
