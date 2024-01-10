from django.db import models

# Create your models here.
class tasklist(models.Model):
    task_name = models.CharField(max_length=200)
    assingned_to = models.CharField(max_length=200)
    assigned_by = models.CharField(max_length=200)
    review = models.BooleanField(default=False)
    priority = models.CharField(max_length=200)
    
    def __str__(self):
        return self.task_name + " -> " + str(self.review)