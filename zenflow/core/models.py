from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('Client', 'Client'),
        ('Freelancer', 'Freelancer'),
        ('ProjectManager', 'Project Manager'),
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    bio = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    rating = models.FloatField(default=0.0)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',  # Unique related_name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions_set',  # Unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Project(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(User, related_name='client_projects', on_delete=models.CASCADE)
    project_manager = models.ForeignKey(User, related_name='managed_projects', on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, related_name='assigned_projects', on_delete=models.CASCADE, null=True, blank=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)

class Task(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected'),
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, related_name='tasks', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    due_date = models.DateField()

class Invoice(models.Model):
    STATUS_CHOICES = (
        ('Unpaid', 'Unpaid'),
        ('Paid', 'Paid'),
    )
    project = models.ForeignKey(Project, related_name='invoices', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)