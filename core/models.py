from django.db import models

# Create your models here.
class users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    created_at = models.DateField().auto_now_add=True

    def __str__(self):
        return self.email
    
    
class tasks(models.Model):
    STATUS_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
    ]

    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(
        users,
        on_delete=models.CASCADE,
        db_column='user_id',
        related_name='tasks'
    )
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendiente')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)    


    def __str__(self):
        return self.title