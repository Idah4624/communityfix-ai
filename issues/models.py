from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):

    CATEGORY_CHOICES = [
        ('road', 'Road'),
        ('electricity', 'Electricity'),
        ('water', 'Water'),
        ('waste', 'Waste Management'),
        ('security', 'Security'),
        ('healthcare', 'Healthcare'),
        ('education', 'Education'),
        ('other', 'Other'),
    ]

    STATUS_CHOICES = [
        ('reported', 'Reported'),
        ('review', 'Under Review'),
        ('progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField()

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='issues/',
        blank=True,
        null=True
    )

    location = models.CharField(max_length=255)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='reported'
    )

    reported_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reported_issues'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title