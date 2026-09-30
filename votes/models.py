from django.db import models
from django.contrib.auth.models import User

from issues.models import Issue


class Vote(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    issue = models.ForeignKey(
        Issue,
        on_delete=models.CASCADE,
        related_name='votes'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'issue'],
                name='unique_user_issue_vote'
            )
        ]

    def __str__(self):
        return f'{self.user.username} - {self.issue.title}'