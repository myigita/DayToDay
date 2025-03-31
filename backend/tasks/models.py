from django.db import models

# Create your models here.

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()

    # default status is pending
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'), 
        ('completed', 'Completed'),
        ('in_progress', 'In Progress'),
        ('postponed', 'Postponed'),
        ('cancelled', 'Cancelled'),
    ], default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    # default is empty
    due_date = models.DateTimeField(null=True, blank=True)
    # 1 max prio, 5 min prio
    priority = models.IntegerField(default=3)

    def __str__(self):
        return self.title