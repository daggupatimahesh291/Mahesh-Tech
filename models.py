

# Create your models here.
from django.db import models 
import datetime
class notes(models.Model):  
    tittle = models.CharField(max_length=20)  
    desc = models.CharField(max_length=100)  
    createdate = models.DateField(_("Date"), default=datetime.date.today)
    updatedate = models.DateField(_("Date"), default=datetime.date.today)  
    class Meta:  
        db_table = "note"  
