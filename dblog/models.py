from django.db import models

class Article(models.Model):
   article = models.TextField()
   post_date = models.DateTimeField('date posted')
   title = models.CharField(maxlength=128)
  
def _str_(self):
 return "Blog(title = '%s')"%(self.title)

class Content(self.Model):

 in_reference_to = models.ForeignKey(Article)
 content = models.TextField(maxlength=256)
 
# Create your models here.
