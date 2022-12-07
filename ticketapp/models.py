from django.db import models

# Create your models here.
class TicketsModels(models.Model):
    task = models.CharField(max_length=200)
    taskno = models.CharField(max_length=200)
    details= models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return "Task={0}, Taskno={1}, Details={2}, Status{3}".format(self.task, self.taskno,self.details,self.status)